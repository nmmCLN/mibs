#
# PySNMP MIB module MITEL-APPLICATION-PLATFORM-LIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-APPLICATION-PLATFORM-LIST-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:36 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mitelIdentification, = mibBuilder.importSymbols("MITEL-MIB", "mitelIdentification")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, MibIdentifier, Gauge32, TimeTicks, Unsigned32, iso, Bits, Counter64, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "TimeTicks", "Unsigned32", "iso", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelIdApplicationPlatforms = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6))
mitelIdApplicationPlatforms.setRevisions(('2014-02-11 12:00', '2006-08-10 00:00', '2005-08-24 21:34',))
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setOrganization('MITEL Networks Corporation')
mitelIdAppPlatManagementApplicationServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 1))
if mibBuilder.loadTexts: mitelIdAppPlatManagementApplicationServer.setStatus('current')
mitelIdAppPlatLXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 2))
if mibBuilder.loadTexts: mitelIdAppPlatLXTelephonyServer.setStatus('current')
mitelIdAppPlatMXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 3))
if mibBuilder.loadTexts: mitelIdAppPlatMXTelephonyServer.setStatus('current')
mitelIdAppPlatCXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 4))
if mibBuilder.loadTexts: mitelIdAppPlatCXTelephonyServer.setStatus('current')
mitelIdAppPlatCXiTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 5))
if mibBuilder.loadTexts: mitelIdAppPlatCXiTelephonyServer.setStatus('current')
mitelIdAppPlatLiteTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 6))
if mibBuilder.loadTexts: mitelIdAppPlatLiteTelephonyServer.setStatus('current')
mitelIdAppPlatMXeTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 7))
if mibBuilder.loadTexts: mitelIdAppPlatMXeTelephonyServer.setStatus('current')
mitelIdAppPlatAXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 8))
if mibBuilder.loadTexts: mitelIdAppPlatAXTelephonyServer.setStatus('current')
mitelIdAppPlatMXTTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 9))
if mibBuilder.loadTexts: mitelIdAppPlatMXTTelephonyServer.setStatus('current')
mibBuilder.exportSymbols("MITEL-APPLICATION-PLATFORM-LIST-MIB", mitelIdAppPlatMXTelephonyServer=mitelIdAppPlatMXTelephonyServer, mitelIdAppPlatManagementApplicationServer=mitelIdAppPlatManagementApplicationServer, mitelIdAppPlatCXiTelephonyServer=mitelIdAppPlatCXiTelephonyServer, mitelIdAppPlatAXTelephonyServer=mitelIdAppPlatAXTelephonyServer, mitelIdAppPlatLXTelephonyServer=mitelIdAppPlatLXTelephonyServer, mitelIdApplicationPlatforms=mitelIdApplicationPlatforms, mitelIdAppPlatMXeTelephonyServer=mitelIdAppPlatMXeTelephonyServer, PYSNMP_MODULE_ID=mitelIdApplicationPlatforms, mitelIdAppPlatLiteTelephonyServer=mitelIdAppPlatLiteTelephonyServer, mitelIdAppPlatMXTTelephonyServer=mitelIdAppPlatMXTTelephonyServer, mitelIdAppPlatCXTelephonyServer=mitelIdAppPlatCXTelephonyServer)
