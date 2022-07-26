#
# PySNMP MIB module ATM-SOFT-PVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-SOFT-PVC-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:21:58 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
atmVclVpi, atmVplVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVplVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, Gauge32, IpAddress, TimeTicks, Integer32, Counter64, Counter32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "ObjectIdentity", "iso")
TextualConvention, DisplayString, TruthValue, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "TimeStamp", "RowStatus")
atmSoftPvcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 353, 5, 5, 1))
atmSoftPvcMIB.setRevisions(('1997-03-01 00:00', '1996-06-21 00:00',))
if mibBuilder.loadTexts: atmSoftPvcMIB.setLastUpdated('9703010000Z')
if mibBuilder.loadTexts: atmSoftPvcMIB.setOrganization('The ATM Forum.')
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumNetworkManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5))
atmfSoftPvc = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5))
atmSoftPvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1))
atmSoftPvcMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
atmSoftPvcBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1))
atmSoftPvcCallFailuresTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSoftPvcCallFailuresTrapEnable.setStatus('current')
atmSoftPvcCallFailures = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCallFailures.setStatus('current')
atmSoftPvcCurrentlyFailingSoftPVccs = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCurrentlyFailingSoftPVccs.setStatus('current')
atmSoftPvcCurrentlyFailingSoftPVpcs = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCurrentlyFailingSoftPVpcs.setStatus('current')
atmSoftPvcNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSoftPvcNotificationInterval.setStatus('current')
atmSoftPVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2), )
if mibBuilder.loadTexts: atmSoftPVccTable.setStatus('current')
atmSoftPVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"))
if mibBuilder.loadTexts: atmSoftPVccEntry.setStatus('current')
atmSoftPVccLeafReference = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atmSoftPVccLeafReference.setStatus('current')
atmSoftPVccTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetAddress.setStatus('current')
atmSoftPVccTargetSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("any", 2))).clone('required')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetSelectType.setStatus('current')
atmSoftPVccTargetVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetVpi.setStatus('current')
atmSoftPVccTargetVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetVci.setStatus('current')
atmSoftPVccLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccLastReleaseCause.setStatus('current')
atmSoftPVccLastReleaseDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccLastReleaseDiagnostic.setStatus('current')
atmSoftPVccOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("establishmentInProgress", 2), ("connected", 3), ("retriesExhausted", 4), ("noAddressSupplied", 5), ("lowerLayerDown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccOperStatus.setStatus('current')
atmSoftPVccRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRestart.setStatus('current')
atmSoftPVccRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryInterval.setStatus('current')
atmSoftPVccRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccRetryTimer.setStatus('current')
atmSoftPVccRetryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryThreshold.setStatus('current')
atmSoftPVccRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccRetryFailures.setStatus('current')
atmSoftPVccRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryLimit.setStatus('current')
atmSoftPVccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRowStatus.setStatus('current')
atmSoftPVpcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3), )
if mibBuilder.loadTexts: atmSoftPVpcTable.setStatus('current')
atmSoftPVpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVplVpi"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"))
if mibBuilder.loadTexts: atmSoftPVpcEntry.setStatus('current')
atmSoftPVpcLeafReference = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63535)))
if mibBuilder.loadTexts: atmSoftPVpcLeafReference.setStatus('current')
atmSoftPVpcTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetAddress.setStatus('current')
atmSoftPVpcTargetSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("any", 2))).clone('required')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetSelectType.setStatus('current')
atmSoftPVpcTargetVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetVpi.setStatus('current')
atmSoftPVpcLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcLastReleaseCause.setStatus('current')
atmSoftPVpcLastReleaseDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcLastReleaseDiagnostic.setStatus('current')
atmSoftPVpcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("establishmentInProgress", 2), ("connected", 3), ("retriesExhausted", 4), ("noAddressSupplied", 5), ("lowerLayerDown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcOperStatus.setStatus('current')
atmSoftPVpcRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRestart.setStatus('current')
atmSoftPVpcRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryInterval.setStatus('current')
atmSoftPVpcRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcRetryTimer.setStatus('current')
atmSoftPVpcRetryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryThreshold.setStatus('current')
atmSoftPVpcRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcRetryFailures.setStatus('current')
atmSoftPVpcRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryLimit.setStatus('current')
atmSoftPVpcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRowStatus.setStatus('current')
atmInterfaceSoftPvcAddressTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4), )
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressTable.setStatus('current')
atmInterfaceSoftPvcAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddress"))
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressEntry.setStatus('current')
atmInterfaceSoftPvcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 1), AtmAddr())
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddress.setStatus('current')
atmInterfaceSoftPvcAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressRowStatus.setStatus('current')
atmCurrentlyFailingSoftPVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5), )
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccTable.setStatus('current')
atmCurrentlyFailingSoftPVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"))
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccEntry.setStatus('current')
atmCurrentlyFailingSoftPVccTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccTimeStamp.setStatus('current')
atmCurrentlyFailingSoftPVpcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6), )
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcTable.setStatus('current')
atmCurrentlyFailingSoftPVpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"))
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcEntry.setStatus('current')
atmCurrentlyFailingSoftPVpcTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcTimeStamp.setStatus('current')
atmSoftPvcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1))
atmSoftPvcTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0))
atmSoftPvcCallFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
if mibBuilder.loadTexts: atmSoftPvcCallFailuresTrap.setStatus('current')
atmSoftPvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3))
atmSoftPvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1))
atmSoftPvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2))
atmSoftPvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcBaseMIBGroup"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcVccMIBGroup"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcAddressMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcMIBCompliance = atmSoftPvcMIBCompliance.setStatus('current')
atmSoftPvcBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailuresTrapEnable"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcNotificationInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcBaseMIBGroup = atmSoftPvcBaseMIBGroup.setStatus('current')
atmSoftPvcVccMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 2)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetAddress"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetSelectType"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVpi"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVci"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseCause"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseDiagnostic"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccOperStatus"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRestart"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryInterval"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryTimer"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryThreshold"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryLimit"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcVccMIBGroup = atmSoftPvcVccMIBGroup.setStatus('current')
atmSoftPvcVpcMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 3)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetAddress"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetSelectType"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetVpi"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseCause"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseDiagnostic"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcOperStatus"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRestart"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryInterval"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryTimer"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryThreshold"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryLimit"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcVpcMIBGroup = atmSoftPvcVpcMIBGroup.setStatus('current')
atmSoftPvcAddressMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 4)).setObjects(("ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddressRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcAddressMIBGroup = atmSoftPvcAddressMIBGroup.setStatus('current')
atmCurrentlyFailingSoftPVccMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 5)).setObjects(("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVccTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmCurrentlyFailingSoftPVccMIBGroup = atmCurrentlyFailingSoftPVccMIBGroup.setStatus('current')
atmCurrentlyFailingSoftPVpcMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 6)).setObjects(("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVpcTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmCurrentlyFailingSoftPVpcMIBGroup = atmCurrentlyFailingSoftPVpcMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ATM-SOFT-PVC-MIB", AtmAddr=AtmAddr, atmSoftPVccEntry=atmSoftPVccEntry, atmSoftPVccLeafReference=atmSoftPVccLeafReference, atmSoftPvcMIBCompliances=atmSoftPvcMIBCompliances, atmSoftPVccTargetAddress=atmSoftPVccTargetAddress, atmSoftPvcCallFailuresTrapEnable=atmSoftPvcCallFailuresTrapEnable, atmSoftPVccRetryThreshold=atmSoftPVccRetryThreshold, atmSoftPvcTrapsPrefix=atmSoftPvcTrapsPrefix, atmInterfaceSoftPvcAddressRowStatus=atmInterfaceSoftPvcAddressRowStatus, atmSoftPVccLastReleaseCause=atmSoftPVccLastReleaseCause, atmSoftPvcMIBConformance=atmSoftPvcMIBConformance, atmSoftPVpcTable=atmSoftPVpcTable, atmSoftPVccRetryTimer=atmSoftPVccRetryTimer, atmSoftPVccRetryInterval=atmSoftPVccRetryInterval, atmSoftPVpcTargetVpi=atmSoftPVpcTargetVpi, atmfSoftPvc=atmfSoftPvc, atmSoftPVccTargetVpi=atmSoftPVccTargetVpi, atmSoftPVpcOperStatus=atmSoftPVpcOperStatus, atmSoftPVpcRestart=atmSoftPVpcRestart, atmCurrentlyFailingSoftPVpcTimeStamp=atmCurrentlyFailingSoftPVpcTimeStamp, atmCurrentlyFailingSoftPVccMIBGroup=atmCurrentlyFailingSoftPVccMIBGroup, atmCurrentlyFailingSoftPVpcEntry=atmCurrentlyFailingSoftPVpcEntry, atmSoftPvcCallFailuresTrap=atmSoftPvcCallFailuresTrap, atmSoftPVpcLeafReference=atmSoftPVpcLeafReference, atmSoftPVccLastReleaseDiagnostic=atmSoftPVccLastReleaseDiagnostic, atmSoftPvcBaseMIBGroup=atmSoftPvcBaseMIBGroup, atmSoftPVpcEntry=atmSoftPVpcEntry, atmSoftPvcCurrentlyFailingSoftPVpcs=atmSoftPvcCurrentlyFailingSoftPVpcs, atmSoftPVccRowStatus=atmSoftPVccRowStatus, atmSoftPVpcRetryInterval=atmSoftPVpcRetryInterval, atmCurrentlyFailingSoftPVpcTable=atmCurrentlyFailingSoftPVpcTable, atmSoftPvcAddressMIBGroup=atmSoftPvcAddressMIBGroup, atmSoftPVccRestart=atmSoftPVccRestart, atmSoftPVpcRetryTimer=atmSoftPVpcRetryTimer, atmSoftPVccTargetSelectType=atmSoftPVccTargetSelectType, atmSoftPVpcLastReleaseCause=atmSoftPVpcLastReleaseCause, atmForumNetworkManagement=atmForumNetworkManagement, atmSoftPvcTraps=atmSoftPvcTraps, atmSoftPvcMIBCompliance=atmSoftPvcMIBCompliance, atmCurrentlyFailingSoftPVpcMIBGroup=atmCurrentlyFailingSoftPVpcMIBGroup, atmSoftPVccTargetVci=atmSoftPVccTargetVci, atmInterfaceSoftPvcAddressEntry=atmInterfaceSoftPvcAddressEntry, atmSoftPVpcTargetAddress=atmSoftPVpcTargetAddress, atmSoftPVpcLastReleaseDiagnostic=atmSoftPVpcLastReleaseDiagnostic, atmSoftPVpcRetryFailures=atmSoftPVpcRetryFailures, atmSoftPVpcTargetSelectType=atmSoftPVpcTargetSelectType, atmSoftPVccOperStatus=atmSoftPVccOperStatus, atmSoftPVpcRetryLimit=atmSoftPVpcRetryLimit, atmSoftPVccTable=atmSoftPVccTable, atmSoftPvcMIBGroups=atmSoftPvcMIBGroups, atmSoftPVpcRetryThreshold=atmSoftPVpcRetryThreshold, atmSoftPvcMIBObjects=atmSoftPvcMIBObjects, atmCurrentlyFailingSoftPVccTable=atmCurrentlyFailingSoftPVccTable, atmSoftPvcBaseGroup=atmSoftPvcBaseGroup, PYSNMP_MODULE_ID=atmSoftPvcMIB, atmSoftPVpcRowStatus=atmSoftPVpcRowStatus, atmSoftPvcCurrentlyFailingSoftPVccs=atmSoftPvcCurrentlyFailingSoftPVccs, atmCurrentlyFailingSoftPVccTimeStamp=atmCurrentlyFailingSoftPVccTimeStamp, atmSoftPvcVpcMIBGroup=atmSoftPvcVpcMIBGroup, atmCurrentlyFailingSoftPVccEntry=atmCurrentlyFailingSoftPVccEntry, atmSoftPVccRetryLimit=atmSoftPVccRetryLimit, atmForum=atmForum, atmInterfaceSoftPvcAddressTable=atmInterfaceSoftPvcAddressTable, atmSoftPvcCallFailures=atmSoftPvcCallFailures, atmSoftPvcNotificationInterval=atmSoftPvcNotificationInterval, atmSoftPVccRetryFailures=atmSoftPVccRetryFailures, atmInterfaceSoftPvcAddress=atmInterfaceSoftPvcAddress, atmSoftPvcMIBTraps=atmSoftPvcMIBTraps, atmSoftPvcMIB=atmSoftPvcMIB, atmSoftPvcVccMIBGroup=atmSoftPvcVccMIBGroup)
