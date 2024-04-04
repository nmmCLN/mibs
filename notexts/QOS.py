#
# PySNMP MIB module QOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/QOS
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:54 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
VlanIdT, QosTagT, EnableStatusT = mibBuilder.importSymbols("ExaltComm", "VlanIdT", "QosTagT", "EnableStatusT")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32, Counter64, NotificationType, Integer32, MibIdentifier, iso, IpAddress, TimeTicks, Gauge32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32", "Counter64", "NotificationType", "Integer32", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class QosPriorityT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3))

class QosModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 5, 6))
    namedValues = NamedValues(("disable", 0), ("qos-mode-802-1p", 4), ("qos-mode-diffserv", 5), ("qos-mode-port", 6))

class QosScheduleModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("weighted-round-robin", 0), ("hybrid1-mode-3sp-2wrr-1wrr-0wrr", 1), ("hybrid2-mode-3sp-2sp-1wrr-0wrr", 2), ("strict-priority", 3))

class QosCos3WeightT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(8, 16, 32))
    namedValues = NamedValues(("w-8", 8), ("w-16", 16), ("w-32", 32))

class QosCos2WeightT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(4, 8, 16))
    namedValues = NamedValues(("w-4", 4), ("w-8", 8), ("w-16", 16))

class QosCos1WeightT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 4, 8))
    namedValues = NamedValues(("w-2", 2), ("w-4", 4), ("w-8", 8))

class QosCos0WeightT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("w-1", 1), ("w-2", 2), ("w-4", 4))

advSystemConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5))
if mibBuilder.loadTexts: advSystemConfig.setStatus('current')
extAirG2QoS = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8))
if mibBuilder.loadTexts: extAirG2QoS.setStatus('current')
qosDefaultQueue = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosDefaultQueue.setStatus('current')
qosEth1Mode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 2), QosModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEth1Mode.setStatus('current')
qosEth2Mode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 3), QosModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEth2Mode.setStatus('current')
qosDiffServList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4), )
if mibBuilder.loadTexts: qosDiffServList.setStatus('current')
qosScheduler = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7))
if mibBuilder.loadTexts: qosScheduler.setStatus('current')
qosDiffServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1), ).setIndexNames((0, "QOS", "diffServValue"), (0, "QOS", "diffServPriority"), (0, "QOS", "diffServEnable"))
if mibBuilder.loadTexts: qosDiffServEntry.setStatus('current')
diffServValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServValue.setStatus('current')
diffServPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 2), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServPriority.setStatus('current')
diffServEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 3), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServEnable.setStatus('current')
qosPortETH1Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5))
qosEth1m802dot1pList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1), )
if mibBuilder.loadTexts: qosEth1m802dot1pList.setStatus('current')
qosEth1m802dot1pEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1), ).setIndexNames((0, "QOS", "tagEth1Priority"), (0, "QOS", "tagEth1Status"))
if mibBuilder.loadTexts: qosEth1m802dot1pEntry.setStatus('current')
tagEth1Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth1Priority.setStatus('current')
tagEth1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth1Status.setStatus('current')
qosEth1PortList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2), )
if mibBuilder.loadTexts: qosEth1PortList.setStatus('current')
qosEth1PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1), ).setIndexNames((0, "QOS", "portEth1Priority"), (0, "QOS", "portEth1Status"))
if mibBuilder.loadTexts: qosEth1PortEntry.setStatus('current')
portEth1Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth1Priority.setStatus('current')
portEth1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth1Status.setStatus('current')
qosPortETH2Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6))
qosEth2m802dot1pList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1), )
if mibBuilder.loadTexts: qosEth2m802dot1pList.setStatus('current')
qosEth2m802dot1pEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1), ).setIndexNames((0, "QOS", "tagEth2Priority"), (0, "QOS", "tagEth2Status"))
if mibBuilder.loadTexts: qosEth2m802dot1pEntry.setStatus('current')
tagEth2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth2Priority.setStatus('current')
tagEth2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth2Status.setStatus('current')
qosEth2PortList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2), )
if mibBuilder.loadTexts: qosEth2PortList.setStatus('current')
qosEth2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1), ).setIndexNames((0, "QOS", "portEth2Priority"), (0, "QOS", "portEth2Status"))
if mibBuilder.loadTexts: qosEth2PortEntry.setStatus('current')
portEth2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth2Priority.setStatus('current')
portEth2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth2Status.setStatus('current')
qosScheduleMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 1), QosScheduleModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosScheduleMode.setStatus('current')
qosCos3Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 2), QosCos3WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos3Weight.setStatus('current')
qosCos2Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 3), QosCos2WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos2Weight.setStatus('current')
qosCos1Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 4), QosCos1WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos1Weight.setStatus('current')
qosCos0Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 5), QosCos0WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos0Weight.setStatus('current')
commitQosSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 1000), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitQosSettings.setStatus('current')
mibBuilder.exportSymbols("QOS", qosScheduler=qosScheduler, qosDiffServEntry=qosDiffServEntry, QosModeT=QosModeT, QosCos3WeightT=QosCos3WeightT, qosEth1m802dot1pEntry=qosEth1m802dot1pEntry, qosCos1Weight=qosCos1Weight, tagEth2Priority=tagEth2Priority, qosDefaultQueue=qosDefaultQueue, QosCos0WeightT=QosCos0WeightT, qosScheduleMode=qosScheduleMode, portEth2Priority=portEth2Priority, qosPortETH2Conf=qosPortETH2Conf, qosEth2PortList=qosEth2PortList, qosEth2Mode=qosEth2Mode, qosCos2Weight=qosCos2Weight, qosEth2PortEntry=qosEth2PortEntry, qosEth1PortList=qosEth1PortList, tagEth1Status=tagEth1Status, QosCos1WeightT=QosCos1WeightT, qosEth1Mode=qosEth1Mode, advSystemConfig=advSystemConfig, commitQosSettings=commitQosSettings, QosScheduleModeT=QosScheduleModeT, diffServPriority=diffServPriority, diffServEnable=diffServEnable, qosEth1PortEntry=qosEth1PortEntry, qosDiffServList=qosDiffServList, portEth1Priority=portEth1Priority, QosCos2WeightT=QosCos2WeightT, QosPriorityT=QosPriorityT, qosEth1m802dot1pList=qosEth1m802dot1pList, diffServValue=diffServValue, tagEth2Status=tagEth2Status, qosCos3Weight=qosCos3Weight, tagEth1Priority=tagEth1Priority, qosEth2m802dot1pEntry=qosEth2m802dot1pEntry, portEth2Status=portEth2Status, extAirG2QoS=extAirG2QoS, qosEth2m802dot1pList=qosEth2m802dot1pList, qosCos0Weight=qosCos0Weight, qosPortETH1Conf=qosPortETH1Conf, portEth1Status=portEth1Status)
