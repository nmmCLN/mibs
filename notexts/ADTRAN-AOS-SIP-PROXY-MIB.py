#
# PySNMP MIB module ADTRAN-AOS-SIP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-SIP-PROXY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:42 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, Gauge32, Unsigned32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Integer32, Counter64, TimeTicks, MibIdentifier, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSSipProxy = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 5))
adGenAOSSipProxy.setRevisions(('2013-05-16 00:00',))
if mibBuilder.loadTexts: adGenAOSSipProxy.setLastUpdated('201305160000Z')
if mibBuilder.loadTexts: adGenAOSSipProxy.setOrganization('ADTRAN, Inc.')
adSipProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5))
adSipProxyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0))
adProxyTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyTimestamp.setStatus('current')
adProxyRolloverFromServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddressType.setStatus('current')
adProxyRolloverFromServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddress.setStatus('current')
adProxyRolloverToServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddressType.setStatus('current')
adProxyRolloverToServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddress.setStatus('current')
class AdProxyRolloverCauseTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("transactionFailed", 1), ("pollFailed", 2), ("pollSucceeded", 3))

adProxyRolloverCause = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 6), AdProxyRolloverCauseTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverCause.setStatus('current')
adSipProxyRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if mibBuilder.loadTexts: adSipProxyRollover.setStatus('current')
adSipProxyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14))
adSipProxyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1))
adSipProxyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2))
adSipProxyFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyFullCompliance = adSipProxyFullCompliance.setStatus('current')
adSipProxyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationGroup = adSipProxyNotificationGroup.setStatus('current')
adSipProxyNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 2)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationUtilityGroup = adSipProxyNotificationUtilityGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-PROXY-MIB", adGenAOSSipProxy=adGenAOSSipProxy, adSipProxyTraps=adSipProxyTraps, adProxyRolloverToServerInetAddress=adProxyRolloverToServerInetAddress, adProxyRolloverFromServerInetAddress=adProxyRolloverFromServerInetAddress, adSipProxyFullCompliance=adSipProxyFullCompliance, adProxyTimestamp=adProxyTimestamp, AdProxyRolloverCauseTC=AdProxyRolloverCauseTC, adSipProxyGroups=adSipProxyGroups, adProxyRolloverToServerInetAddressType=adProxyRolloverToServerInetAddressType, adSipProxyCompliances=adSipProxyCompliances, adSipProxyNotificationUtilityGroup=adSipProxyNotificationUtilityGroup, adSipProxyNotificationGroup=adSipProxyNotificationGroup, adSipProxyConformance=adSipProxyConformance, adSipProxyRollover=adSipProxyRollover, PYSNMP_MODULE_ID=adGenAOSSipProxy, adProxyRolloverCause=adProxyRolloverCause, adProxyRolloverFromServerInetAddressType=adProxyRolloverFromServerInetAddressType, adSipProxy=adSipProxy)
