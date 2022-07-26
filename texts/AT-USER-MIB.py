#
# PySNMP MIB module AT-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-USER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:05 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, ModuleIdentity, Counter64, MibIdentifier, Gauge32, iso, Integer32, Counter32, IpAddress, Bits, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibIdentifier", "Gauge32", "iso", "Integer32", "Counter32", "IpAddress", "Bits", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
user = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20))
user.setRevisions(('2012-09-21 00:00', '2010-09-07 00:00', '2010-06-15 00:15', '2010-06-08 00:00', '2008-10-16 12:00', '2008-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: user.setRevisionsDescriptions(('Added chassis switch (e.g. SBx8100) descriptions to stack-related MIB objects', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Add objects for strong passwords information.', 'Add objects for local user data base information.', 'Initial version.',))
if mibBuilder.loadTexts: user.setLastUpdated('201209210000Z')
if mibBuilder.loadTexts: user.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: user.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: user.setDescription('The AT-USER MIB contains objects for displaying information of\n                users currently logged into a device, or configured in the local\n                user data base of the device.')
userInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1), )
if mibBuilder.loadTexts: userInfoTable.setStatus('current')
if mibBuilder.loadTexts: userInfoTable.setDescription('A table of information about users. Each entry in the table\n                represents a user currently logged into the device.')
userInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1), ).setIndexNames((0, "AT-USER-MIB", "userInfoType"), (0, "AT-USER-MIB", "userInfoIndex"))
if mibBuilder.loadTexts: userInfoEntry.setStatus('current')
if mibBuilder.loadTexts: userInfoEntry.setDescription('Information on a user currently logged into the device.')
userInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("console", 1), ("aux", 2), ("telnet", 3), ("script", 4), ("stack", 5))))
if mibBuilder.loadTexts: userInfoType.setStatus('current')
if mibBuilder.loadTexts: userInfoType.setDescription('The type of connection through which the user logged into\n                the device:\n                - console (1)\n                - aux (2)\n                - telnet (3)\n                - script (4)\n                - stack or back-up CFC console (5)')
userInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: userInfoIndex.setStatus('current')
if mibBuilder.loadTexts: userInfoIndex.setDescription('The index of the line upon which the user logged into\n                the device.')
userInfoUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoUserName.setStatus('current')
if mibBuilder.loadTexts: userInfoUserName.setDescription('This object represents the user name of the user\n                currently logged into the device.')
userInfoPrivilegeLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPrivilegeLevel.setStatus('current')
if mibBuilder.loadTexts: userInfoPrivilegeLevel.setDescription('This object indicates the privilege level the user is granted.')
userInfoIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoIdleTime.setStatus('current')
if mibBuilder.loadTexts: userInfoIdleTime.setDescription('This object indicates the amount of time since the user was last\n                active. It is in the form of hh:mm:ss.')
userInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoLocation.setStatus('current')
if mibBuilder.loadTexts: userInfoLocation.setDescription('This object indicates the location or login method of the user.\n                It can be an IP address used by the user to telnet into the device,\n                or an asyn port, etc.')
userInfoPasswordLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPasswordLifetime.setStatus('current')
if mibBuilder.loadTexts: userInfoPasswordLifetime.setDescription("This object indicates the number of days remaining until the users\n                password expires.  Depending on the current user setting it will\n                either display a string of:\n                'No Expiry' - password will never expire (default);\n                'x days' where x is the remaining lifetime of the current password - the\n                 maximum lifetime value is 1000 days;\n                '-x days (expired)' indicates that the current password expired 'x' days ago.")
userInfoPasswordLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPasswordLastChange.setStatus('current')
if mibBuilder.loadTexts: userInfoPasswordLastChange.setDescription('This object indicates, in days, the last time the password was\n                altered.')
userConfigTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2), )
if mibBuilder.loadTexts: userConfigTable.setStatus('current')
if mibBuilder.loadTexts: userConfigTable.setDescription('A table of user configuration information. Each entry\n                in the table represents a user configured in the local user\n                data base of the device.')
userConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1), ).setIndexNames((0, "AT-USER-MIB", "userConfigIndex"))
if mibBuilder.loadTexts: userConfigEntry.setStatus('current')
if mibBuilder.loadTexts: userConfigEntry.setDescription('A conceptual entry in the userConfigTable.')
userConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: userConfigIndex.setStatus('current')
if mibBuilder.loadTexts: userConfigIndex.setDescription('The index used to identify entries in the userConfigTable.')
userConfigUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userConfigUsername.setStatus('current')
if mibBuilder.loadTexts: userConfigUsername.setDescription("This object represents the user's name in configuration.")
userConfigPrivilegeLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userConfigPrivilegeLevel.setStatus('current')
if mibBuilder.loadTexts: userConfigPrivilegeLevel.setDescription("This object represents the user's privilege level in configuration.")
userSecurityPasswordRules = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3))
userSecurityPasswordHistory = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordHistory.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordHistory.setDescription("This object represents the number of previous passwords that will be\n                retained for comparison when a new password is created for the user.\n                The password must be unique when compared against the previous history.\n                A value of 0 represents 'No Restriction' - default.\n                The maximum number of retained passwords is 15.")
userSecurityPasswordLifetime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordLifetime.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordLifetime.setDescription("This object represents the maximum time interval (days) that the\n                password may persist for before a change is required.\n                A value of 0 represents 'No Expiry' - default.\n                The maximum value is 1000 days.")
userSecurityPasswordWarning = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordWarning.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordWarning.setDescription("This object represents the number of days before the password\n                expires that a warning message will be displayed when the user logs on.\n                A value of 0 indicates 'No Warning' - default.\n                The maximum value is 1000 but must always be less than the password\n                lifetime.")
userSecurityPasswordMinLength = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordMinLength.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordMinLength.setDescription('This object represents the minimum password length that the password\n                must satisfy to be considered valid.\n                The default value is 1.')
userSecurityPasswordMinCategory = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordMinCategory.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordMinCategory.setDescription('This object represents the minimum number of different categories\n                that the password must satisfy to be considered valid.\n                Categories are split into four groups:\n                  upper-case letters; lower-case letters; digits; special symbols.\n                For example, combinations of: ABCD (1 category), ABCDabcd (2 categories),\n                ABCD1111 (2 categories), abcd#$# (2 categories), Aa1# (4 categories).\n                The default value is 1.')
userSecurityPasswordForced = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordForced.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordForced.setDescription('This object represents whether or not a user with an expired password\n                should be forced to alter their password at the next log-on.  When a user\n                logs on with an expired password the system will either reject the log-on\n                attempt or if allowed to log-on then the user may be forced to update\n                their password immediately depending on this setting.\n                This functionality is only valid for administrative users.\n                The default value is disabled.')
userSecurityPasswordReject = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordReject.setStatus('current')
if mibBuilder.loadTexts: userSecurityPasswordReject.setDescription('This object represents whether or not a user log-on attempt with an expired\n                password will be rejected.  If they are not rejected then the user will\n                be allowed to log-on.  They may have to alter their password immediately\n                based on the forced setting.\n                This functionality is only valid for administrative users.  The passwords of\n                non-administrative users will never expire.\n                The default value is disabled.')
mibBuilder.exportSymbols("AT-USER-MIB", userInfoPrivilegeLevel=userInfoPrivilegeLevel, userInfoPasswordLastChange=userInfoPasswordLastChange, userInfoTable=userInfoTable, userConfigIndex=userConfigIndex, userConfigPrivilegeLevel=userConfigPrivilegeLevel, userInfoIdleTime=userInfoIdleTime, userInfoPasswordLifetime=userInfoPasswordLifetime, userInfoType=userInfoType, userConfigUsername=userConfigUsername, userSecurityPasswordMinLength=userSecurityPasswordMinLength, userSecurityPasswordRules=userSecurityPasswordRules, userSecurityPasswordLifetime=userSecurityPasswordLifetime, userSecurityPasswordWarning=userSecurityPasswordWarning, userConfigEntry=userConfigEntry, userInfoEntry=userInfoEntry, PYSNMP_MODULE_ID=user, userSecurityPasswordReject=userSecurityPasswordReject, user=user, userInfoLocation=userInfoLocation, userSecurityPasswordHistory=userSecurityPasswordHistory, userInfoIndex=userInfoIndex, userSecurityPasswordMinCategory=userSecurityPasswordMinCategory, userConfigTable=userConfigTable, userSecurityPasswordForced=userSecurityPasswordForced, userInfoUserName=userInfoUserName)
