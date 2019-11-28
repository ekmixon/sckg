# platform = multi_platform_all
# complexity = low
# reboot = false
# disruption = low
# strategy = disable

# CAUTION: This remediation script will remove tftp-server
#	   from the system, and may remove any packages
#	   that depend on tftp-server. Execute this
#	   remediation AFTER testing on a non-production
#	   system!

if rpm -q --quiet "tftp-server" ; then
    yum remove -y "tftp-server"
fi