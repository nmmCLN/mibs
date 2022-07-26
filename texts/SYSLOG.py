#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.8 at Tue Jul 26 15:39:27 2022
# On host fv-az299-344 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogFilterSelectT, SyslogEnableT = mibBuilder.importSymbols("ExaltComm", "SyslogFilterSelectT", "SyslogEnableT")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Bits, TimeTicks, MibIdentifier, IpAddress, Counter32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
advSystemConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5))
if mibBuilder.loadTexts: advSystemConfig.setStatus('current')
if mibBuilder.loadTexts: advSystemConfig.setDescription('This is the device specific advanced configuration section.')
syslogCfg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6))
if mibBuilder.loadTexts: syslogCfg.setStatus('current')
if mibBuilder.loadTexts: syslogCfg.setDescription('Syslog remote logging configuration.')
syslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1), SyslogEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogEnable.setStatus('current')
if mibBuilder.loadTexts: syslogEnable.setDescription('this mib to enable/disable the Syslog remote logging in the radio.\n\t                     0 - disbale Syslog remote logging. \n\t\t\t     1 - enable Syslog remote logging.')
syslogRemoteIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRemoteIpAddr.setStatus('current')
if mibBuilder.loadTexts: syslogRemoteIpAddr.setDescription('IP address of the remote host the Syslog event messages being sent to.\n\t                     IP address is in xxx.xxx.xxx.xxx format')
syslogFilterSelect = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 3), SyslogFilterSelectT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogFilterSelect.setStatus('current')
if mibBuilder.loadTexts: syslogFilterSelect.setDescription('logging filter selection.\n\t                   \n\t\t\t    0 - All - send all event messages to remote                    \n\t\t\t    1 - Minor - Minor only                 \n\t\t\t    2 - Minor, Major and critical                  \n\t\t\t    3 - Major only          \n\t\t\t    4 - Major and Critical                \n\t\t\t    5 - Critical only.')
commitSyslogSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1000), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitSyslogSettings.setStatus('current')
if mibBuilder.loadTexts: commitSyslogSettings.setDescription('This command allows saving or clear the Syslog configuration.\n                            Option strings to be written are: save, clear, correspondingly saving changes to\n                            configuration to the persistent storage or clearing unsaved changes.')
mibBuilder.exportSymbols("SYSLOG", syslogFilterSelect=syslogFilterSelect, advSystemConfig=advSystemConfig, syslogCfg=syslogCfg, syslogRemoteIpAddr=syslogRemoteIpAddr, syslogEnable=syslogEnable, commitSyslogSettings=commitSyslogSettings)
