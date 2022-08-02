
from lxml import objectify

from sckg.etl.generic import Generic

class DoDCCI(Generic):

  def __init__(self, config):
    super().__init__(config)

  def extract(self, regime, parsable_document):
    with open(parsable_document, 'r') as f:
      xml = f.read()

    root = objectify.fromstring(xml)

    j = []
    for item in root.cci_items.cci_item:
      id = item.attrib.get('id', '')
      control_list = [
          reference.attrib.get('index')
          for reference in item.references.reference
      ]
      j.append({
        'id': id,
        'controls': control_list
      })

    return j

  def transform(self, regime, regime_list):
    regime_name = regime['description']
    updated = regime['meta']['updated']

    stmts = [self.create_regime(regime_name)]
    stmts.append(
        self.create_regime_baseline(regime_name,
                                    properties={
                                      'name': updated
                                    })
    )
    for cci in regime_list:
      name = cci['id']
      controls = cci['controls']
      stmts.append(
          self.create_geneirc_control(regime_name,
                                      'baseline',
                                      updated,
                                      properties={
                                        'name': name
                                      })
      )
      corrected_controls = []
      for control in controls:
        if ' ' in control and '(' not in control:
          control = control.replace(' ', '', 1).replace(' ', '.') + '.'
        corrected_controls.append(control)
      stmts.extend(
          self.create_control_control_map(
              names={
                  'by_regime': True,
                  'mapping_regime': 'DoD CCI',
                  'mapping_control': name,
                  'mapped_regime': 'NIST 800-53',
                  'mapped_control': control,
                  'relationship': 'REFERENCES',
              },
              properties={},
          ) for control in corrected_controls)
    return stmts




