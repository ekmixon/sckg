# platform = multi_platform_all
# complexity = low
# reboot = false
# disruption = low
# strategy = disable

# CAUTION: This remediation script will remove abrt-plugin-logger
#	   from the system, and may remove any packages
#	   that depend on abrt-plugin-logger. Execute this
#	   remediation AFTER testing on a non-production
#	   system!

if rpm -q --quiet "abrt-plugin-logger" ; then
    yum remove -y "abrt-plugin-logger"
fi