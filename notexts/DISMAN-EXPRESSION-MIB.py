#
# PySNMP MIB module DISMAN-EXPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC2982-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
mib_2, ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, zeroDotZero, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "zeroDotZero", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TruthValue, TimeStamp, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention", "RowStatus")
dismanExpressionMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 90))
dismanExpressionMIB.setRevisions(('2000-10-16 00:00',))
if mibBuilder.loadTexts: dismanExpressionMIB.setLastUpdated('200010160000Z')
if mibBuilder.loadTexts: dismanExpressionMIB.setOrganization('IETF Distributed Management Working Group')
dismanExpressionMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 1))
expResource = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 1, 1))
expDefine = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 1, 2))
expValue = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 1, 3))
expResourceDeltaMinimum = MibScalar((1, 3, 6, 1, 2, 1, 90, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 600), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: expResourceDeltaMinimum.setStatus('current')
expResourceDeltaWildcardInstanceMaximum = MibScalar((1, 3, 6, 1, 2, 1, 90, 1, 1, 2), Unsigned32()).setUnits('instances').setMaxAccess("readwrite")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstanceMaximum.setStatus('current')
expResourceDeltaWildcardInstances = MibScalar((1, 3, 6, 1, 2, 1, 90, 1, 1, 3), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstances.setStatus('current')
expResourceDeltaWildcardInstancesHigh = MibScalar((1, 3, 6, 1, 2, 1, 90, 1, 1, 4), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstancesHigh.setStatus('current')
expResourceDeltaWildcardInstanceResourceLacks = MibScalar((1, 3, 6, 1, 2, 1, 90, 1, 1, 5), Counter32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstanceResourceLacks.setStatus('current')
expExpressionTable = MibTable((1, 3, 6, 1, 2, 1, 90, 1, 2, 1), )
if mibBuilder.loadTexts: expExpressionTable.setStatus('current')
expExpressionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1), ).setIndexNames((0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"), (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"))
if mibBuilder.loadTexts: expExpressionEntry.setStatus('current')
expExpressionOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: expExpressionOwner.setStatus('current')
expExpressionName = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: expExpressionName.setStatus('current')
expExpression = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpression.setStatus('current')
expExpressionValueType = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8))).clone('counter32')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpressionValueType.setStatus('current')
expExpressionComment = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 5), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpressionComment.setStatus('current')
expExpressionDeltaInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpressionDeltaInterval.setStatus('current')
expExpressionPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionPrefix.setStatus('current')
expExpressionErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionErrors.setStatus('current')
expExpressionEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpressionEntryStatus.setStatus('current')
expErrorTable = MibTable((1, 3, 6, 1, 2, 1, 90, 1, 2, 2), )
if mibBuilder.loadTexts: expErrorTable.setStatus('current')
expErrorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1), ).setIndexNames((0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"), (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"))
if mibBuilder.loadTexts: expErrorEntry.setStatus('current')
expErrorTime = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expErrorTime.setStatus('current')
expErrorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expErrorIndex.setStatus('current')
expErrorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("invalidSyntax", 1), ("undefinedObjectIndex", 2), ("unrecognizedOperator", 3), ("unrecognizedFunction", 4), ("invalidOperandType", 5), ("unmatchedParenthesis", 6), ("tooManyWildcardValues", 7), ("recursion", 8), ("deltaTooShort", 9), ("resourceUnavailable", 10), ("divideByZero", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: expErrorCode.setStatus('current')
expErrorInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expErrorInstance.setStatus('current')
expObjectTable = MibTable((1, 3, 6, 1, 2, 1, 90, 1, 2, 3), )
if mibBuilder.loadTexts: expObjectTable.setStatus('current')
expObjectEntry = MibTableRow((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1), ).setIndexNames((0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"), (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"), (0, "DISMAN-EXPRESSION-MIB", "expObjectIndex"))
if mibBuilder.loadTexts: expObjectEntry.setStatus('current')
expObjectIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: expObjectIndex.setStatus('current')
expObjectID = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectID.setStatus('current')
expObjectIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectIDWildcard.setStatus('current')
expObjectSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("changedValue", 3))).clone('absoluteValue')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectSampleType.setStatus('current')
sysUpTimeInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 3, 0))
expObjectDeltaDiscontinuityID = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 5), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 1, 3, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDeltaDiscontinuityID.setStatus('current')
expObjectDiscontinuityIDWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDiscontinuityIDWildcard.setStatus('current')
expObjectDiscontinuityIDType = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("timeTicks", 1), ("timeStamp", 2), ("dateAndTime", 3))).clone('timeTicks')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDiscontinuityIDType.setStatus('current')
expObjectConditional = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 8), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectConditional.setStatus('current')
expObjectConditionalWildcard = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectConditionalWildcard.setStatus('current')
expObjectEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectEntryStatus.setStatus('current')
expValueTable = MibTable((1, 3, 6, 1, 2, 1, 90, 1, 3, 1), )
if mibBuilder.loadTexts: expValueTable.setStatus('current')
expValueEntry = MibTableRow((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1), ).setIndexNames((0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"), (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"), (1, "DISMAN-EXPRESSION-MIB", "expValueInstance"))
if mibBuilder.loadTexts: expValueEntry.setStatus('current')
expValueInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: expValueInstance.setStatus('current')
expValueCounter32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueCounter32Val.setStatus('current')
expValueUnsigned32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueUnsigned32Val.setStatus('current')
expValueTimeTicksVal = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueTimeTicksVal.setStatus('current')
expValueInteger32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueInteger32Val.setStatus('current')
expValueIpAddressVal = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueIpAddressVal.setStatus('current')
expValueOctetStringVal = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueOctetStringVal.setStatus('current')
expValueOidVal = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueOidVal.setStatus('current')
expValueCounter64Val = MibTableColumn((1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueCounter64Val.setStatus('current')
dismanExpressionMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 3))
dismanExpressionMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 3, 1))
dismanExpressionMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 90, 3, 2))
dismanExpressionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 90, 3, 1, 1)).setObjects(("DISMAN-EXPRESSION-MIB", "dismanExpressionResourceGroup"), ("DISMAN-EXPRESSION-MIB", "dismanExpressionDefinitionGroup"), ("DISMAN-EXPRESSION-MIB", "dismanExpressionValueGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanExpressionMIBCompliance = dismanExpressionMIBCompliance.setStatus('current')
dismanExpressionResourceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 90, 3, 2, 1)).setObjects(("DISMAN-EXPRESSION-MIB", "expResourceDeltaMinimum"), ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceMaximum"), ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstances"), ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstancesHigh"), ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceResourceLacks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanExpressionResourceGroup = dismanExpressionResourceGroup.setStatus('current')
dismanExpressionDefinitionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 90, 3, 2, 2)).setObjects(("DISMAN-EXPRESSION-MIB", "expExpression"), ("DISMAN-EXPRESSION-MIB", "expExpressionValueType"), ("DISMAN-EXPRESSION-MIB", "expExpressionComment"), ("DISMAN-EXPRESSION-MIB", "expExpressionDeltaInterval"), ("DISMAN-EXPRESSION-MIB", "expExpressionPrefix"), ("DISMAN-EXPRESSION-MIB", "expExpressionErrors"), ("DISMAN-EXPRESSION-MIB", "expExpressionEntryStatus"), ("DISMAN-EXPRESSION-MIB", "expErrorTime"), ("DISMAN-EXPRESSION-MIB", "expErrorIndex"), ("DISMAN-EXPRESSION-MIB", "expErrorCode"), ("DISMAN-EXPRESSION-MIB", "expErrorInstance"), ("DISMAN-EXPRESSION-MIB", "expObjectID"), ("DISMAN-EXPRESSION-MIB", "expObjectIDWildcard"), ("DISMAN-EXPRESSION-MIB", "expObjectSampleType"), ("DISMAN-EXPRESSION-MIB", "expObjectDeltaDiscontinuityID"), ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDWildcard"), ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDType"), ("DISMAN-EXPRESSION-MIB", "expObjectConditional"), ("DISMAN-EXPRESSION-MIB", "expObjectConditionalWildcard"), ("DISMAN-EXPRESSION-MIB", "expObjectEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanExpressionDefinitionGroup = dismanExpressionDefinitionGroup.setStatus('current')
dismanExpressionValueGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 90, 3, 2, 3)).setObjects(("DISMAN-EXPRESSION-MIB", "expValueCounter32Val"), ("DISMAN-EXPRESSION-MIB", "expValueUnsigned32Val"), ("DISMAN-EXPRESSION-MIB", "expValueTimeTicksVal"), ("DISMAN-EXPRESSION-MIB", "expValueInteger32Val"), ("DISMAN-EXPRESSION-MIB", "expValueIpAddressVal"), ("DISMAN-EXPRESSION-MIB", "expValueOctetStringVal"), ("DISMAN-EXPRESSION-MIB", "expValueOidVal"), ("DISMAN-EXPRESSION-MIB", "expValueCounter64Val"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dismanExpressionValueGroup = dismanExpressionValueGroup.setStatus('current')
mibBuilder.exportSymbols("DISMAN-EXPRESSION-MIB", expExpressionPrefix=expExpressionPrefix, dismanExpressionMIBObjects=dismanExpressionMIBObjects, expExpressionValueType=expExpressionValueType, expValueInstance=expValueInstance, expErrorEntry=expErrorEntry, expErrorInstance=expErrorInstance, expValueEntry=expValueEntry, expValueOctetStringVal=expValueOctetStringVal, expObjectEntryStatus=expObjectEntryStatus, dismanExpressionMIBCompliances=dismanExpressionMIBCompliances, expObjectDiscontinuityIDWildcard=expObjectDiscontinuityIDWildcard, expResource=expResource, expExpressionName=expExpressionName, expResourceDeltaWildcardInstances=expResourceDeltaWildcardInstances, expValueTimeTicksVal=expValueTimeTicksVal, dismanExpressionResourceGroup=dismanExpressionResourceGroup, expValueCounter32Val=expValueCounter32Val, expErrorTime=expErrorTime, expObjectIndex=expObjectIndex, dismanExpressionMIBCompliance=dismanExpressionMIBCompliance, expExpressionDeltaInterval=expExpressionDeltaInterval, expErrorCode=expErrorCode, expExpressionTable=expExpressionTable, dismanExpressionMIB=dismanExpressionMIB, expObjectIDWildcard=expObjectIDWildcard, expExpression=expExpression, expObjectDiscontinuityIDType=expObjectDiscontinuityIDType, expValueCounter64Val=expValueCounter64Val, expResourceDeltaWildcardInstancesHigh=expResourceDeltaWildcardInstancesHigh, expErrorTable=expErrorTable, expObjectConditional=expObjectConditional, expValueTable=expValueTable, dismanExpressionMIBConformance=dismanExpressionMIBConformance, dismanExpressionMIBGroups=dismanExpressionMIBGroups, expExpressionErrors=expExpressionErrors, expObjectDeltaDiscontinuityID=expObjectDeltaDiscontinuityID, expResourceDeltaWildcardInstanceResourceLacks=expResourceDeltaWildcardInstanceResourceLacks, expResourceDeltaMinimum=expResourceDeltaMinimum, expObjectSampleType=expObjectSampleType, expExpressionOwner=expExpressionOwner, expDefine=expDefine, expValueIpAddressVal=expValueIpAddressVal, expExpressionEntryStatus=expExpressionEntryStatus, sysUpTimeInstance=sysUpTimeInstance, expExpressionComment=expExpressionComment, expValueOidVal=expValueOidVal, expObjectConditionalWildcard=expObjectConditionalWildcard, expValueUnsigned32Val=expValueUnsigned32Val, dismanExpressionValueGroup=dismanExpressionValueGroup, dismanExpressionDefinitionGroup=dismanExpressionDefinitionGroup, expObjectID=expObjectID, expResourceDeltaWildcardInstanceMaximum=expResourceDeltaWildcardInstanceMaximum, expErrorIndex=expErrorIndex, PYSNMP_MODULE_ID=dismanExpressionMIB, expExpressionEntry=expExpressionEntry, expObjectEntry=expObjectEntry, expValue=expValue, expObjectTable=expObjectTable, expValueInteger32Val=expValueInteger32Val)
