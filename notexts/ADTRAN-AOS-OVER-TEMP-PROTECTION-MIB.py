#
# PySNMP MIB module ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 16:39:18 2022
# On host fv-az545-99 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, NotificationType, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSOverTempProtectionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 10))
adGenAOSOverTempProtectionMib.setRevisions(('2014-11-04 16:15',))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setLastUpdated('201411041615Z')
if mibBuilder.loadTexts: adGenAOSOverTempProtectionMib.setOrganization('ADTRAN, Inc.')
adGenAOSOverTempProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10))
adGenAOSOverTempProtectionTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0))
adGenAOSOverTempProtectionWarning = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 1))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionWarning.setStatus('current')
adGenAOSOverTempProtectionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10, 0, 2))
if mibBuilder.loadTexts: adGenAOSOverTempProtectionShutdown.setStatus('current')
adGenAOSOverTempProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19))
adGenAOSOverTempProtectionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1))
adGenAOSOverTempProtectionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2))
adGenAOSOverTempProtectionFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 2, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionFullCompliance = adGenAOSOverTempProtectionFullCompliance.setStatus('current')
adGenAOSOverTempProtectionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 19, 1, 1)).setObjects(("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionWarning"), ("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", "adGenAOSOverTempProtectionShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSOverTempProtectionNotificationGroup = adGenAOSOverTempProtectionNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-OVER-TEMP-PROTECTION-MIB", adGenAOSOverTempProtectionNotificationGroup=adGenAOSOverTempProtectionNotificationGroup, adGenAOSOverTempProtectionGroups=adGenAOSOverTempProtectionGroups, adGenAOSOverTempProtectionMib=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSOverTempProtectionConformance=adGenAOSOverTempProtectionConformance, adGenAOSOverTempProtectionShutdown=adGenAOSOverTempProtectionShutdown, PYSNMP_MODULE_ID=adGenAOSOverTempProtectionMib, adGenAOSOverTempProtectionCompliances=adGenAOSOverTempProtectionCompliances, adGenAOSOverTempProtectionTrap=adGenAOSOverTempProtectionTrap, adGenAOSOverTempProtectionWarning=adGenAOSOverTempProtectionWarning, adGenAOSOverTempProtectionFullCompliance=adGenAOSOverTempProtectionFullCompliance)
