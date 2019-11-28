# platform = multi_platform_all
# complexity = low
# reboot = false
# disruption = low
# strategy = disable

# CAUTION: This remediation script will remove iprutils
#	   from the system, and may remove any packages
#	   that depend on iprutils. Execute this
#	   remediation AFTER testing on a non-production
#	   system!

if rpm -q --quiet "iprutils" ; then
    yum remove -y "iprutils"
fi