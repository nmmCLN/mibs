#
# PySNMP MIB module ARRIS-C3-FPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-FPD-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:59 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, iso, TimeTicks, Bits, IpAddress, Unsigned32, Integer32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "iso", "TimeTicks", "Bits", "IpAddress", "Unsigned32", "Integer32", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmtsC3FPDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3))
if mibBuilder.loadTexts: cmtsC3FPDMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3FPDMIB.setOrganization('Arris International')
if mibBuilder.loadTexts: cmtsC3FPDMIB.setContactInfo('   Network Management\n                Postal: Arris International.\n                        4400 Cork Airport Business Park\n                        Cork Airport, Kinsale Road\n                        Cork, Ireland.\n                Tel:    +353 21 7305 800\n                Fax:    +353 21 4321 972')
if mibBuilder.loadTexts: cmtsC3FPDMIB.setDescription('This MIB manages the Front Panel Display (FPD)\n            software on the Arris CMTS C3')
dcxFPDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1))
dcxFPDMsgTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1), )
if mibBuilder.loadTexts: dcxFPDMsgTable.setStatus('current')
if mibBuilder.loadTexts: dcxFPDMsgTable.setDescription('Table of Front Panel LCD Messages.')
dcxFPDMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-FPD-MIB", "dcxFPDMsgIndex"))
if mibBuilder.loadTexts: dcxFPDMsgEntry.setStatus('current')
if mibBuilder.loadTexts: dcxFPDMsgEntry.setDescription('.')
dcxFPDMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: dcxFPDMsgIndex.setStatus('current')
if mibBuilder.loadTexts: dcxFPDMsgIndex.setDescription('Index used to order the FPD Messages.')
dcxFPDMsgString = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFPDMsgString.setStatus('current')
if mibBuilder.loadTexts: dcxFPDMsgString.setDescription('Specifies a string that can be displayed\n            on the front panel.')
dcxFPDControlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2))
dcxFPDAttachedStatus = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("attached", 1), ("detached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDAttachedStatus.setStatus('current')
if mibBuilder.loadTexts: dcxFPDAttachedStatus.setDescription('Displays if the front panel display is \n            attached to the Cmts or not.')
dcxFPDPowerStatus1 = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDPowerStatus1.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPowerStatus1.setDescription('Specifies if the primary power supply is\n            working.  This is the rightmost power supply.\n            The following values are possible:\n            on(1) and off(2)')
dcxFPDPowerStatus2 = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDPowerStatus2.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPowerStatus2.setDescription('Specifies if the secondary power supply is \n            working.  This is the leftmost power supply(nearest the fan tray).\n            The following values are possible:\n            on(1) and off(2)')
dcxFPDTemp1Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDTemp1Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTemp1Status.setDescription('Specifies the temperature reading for the\n            sensor on the CPU card closest to the CPU.')
dcxFPDTemp2Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDTemp2Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTemp2Status.setDescription('Specifies the temperature reading for the\n            sensor on the CPU card, on the right hand side.')
dcxFPDTemp3Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDTemp3Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTemp3Status.setDescription('Specifies the temperature reading for the\n            sensor on the Kanga card under the Roo cards\n            between RX4 and RX5.')
dcxFPDTemp4Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDTemp4Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTemp4Status.setDescription('Specifies the temperature reading for the\n            sensor on the Kanga card under the Roo cards\n            between RX2 and RX3.')
dcxFPDFan1Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan1Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan1Status.setDescription('Specifies the fan status for the fan nearest the front of the box.\n            The following values are possible: \n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFan2Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan2Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan2Status.setDescription('Specifies the fan status for the fan 2nd from the front.\n            The following values are possible:\n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFan3Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan3Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan3Status.setDescription('Specifies the fan status for the fan 3rd from the front.\n            The following values are possible: \n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFan4Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan4Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan4Status.setDescription('Specifies the fan status for the fan 4th from the front.\n            The following values are possible:\n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFan5Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan5Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan5Status.setDescription('Specifies the fan status for the fan 5th from the front.\n            The following values are possible:\n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFan6Status = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rotating", 1), ("badRotating", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDFan6Status.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan6Status.setDescription('Specifies the fan status for the fan nearest the back of the box\n            The following values are possible:\n            Rotating(1) and BadRotating(2).\n            BadRotating is set when the fan is operating outside of dcxFPDFanUpperLimit and dcxFPDFanLowerLimit.')
dcxFPDFanUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFPDFanUpperLimit.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFanUpperLimit.setDescription('Specifies the upper fan limit(Upper threshold of expected current draw)')
dcxFPDFanLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFPDFanLowerLimit.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFanLowerLimit.setDescription('Specifies the lower fan limit(Lower threshold of expected current draw)')
dcxFPDLCDContrast = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFPDLCDContrast.setStatus('current')
if mibBuilder.loadTexts: dcxFPDLCDContrast.setDescription('Specifies the contrast level for the LCD')
dcxFPDLedSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFPDLedSetStatus.setStatus('current')
if mibBuilder.loadTexts: dcxFPDLedSetStatus.setDescription('Used to turn on or off a Led on the front panel')
dcxFPDHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDHwRevision.setStatus('current')
if mibBuilder.loadTexts: dcxFPDHwRevision.setDescription('Specifies the front panel h/w revision')
dcxFPDSwRevision = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFPDSwRevision.setStatus('current')
if mibBuilder.loadTexts: dcxFPDSwRevision.setDescription('Specifies the front panel s/w revision')
dcxFPDTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3))
dcxFPDAttached = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 1))
if mibBuilder.loadTexts: dcxFPDAttached.setStatus('current')
if mibBuilder.loadTexts: dcxFPDAttached.setDescription('Front Panel Display has been attached.')
dcxFPDDetached = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 2))
if mibBuilder.loadTexts: dcxFPDDetached.setStatus('current')
if mibBuilder.loadTexts: dcxFPDDetached.setDescription('Front Panel Display has been detached.')
dcxFPDFan1Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 3))
if mibBuilder.loadTexts: dcxFPDFan1Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan1Fail.setDescription('Fan nearest the front of the box failed')
dcxFPDFan1FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 4))
if mibBuilder.loadTexts: dcxFPDFan1FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan1FailClr.setDescription('Fan nearest the front of the box is working')
dcxFPDFan2Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 5))
if mibBuilder.loadTexts: dcxFPDFan2Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan2Fail.setDescription('Fan 2nd from the front failed')
dcxFPDFan2FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 6))
if mibBuilder.loadTexts: dcxFPDFan2FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan2FailClr.setDescription('Fan 2nd from the front is working')
dcxFPDFan3Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 7))
if mibBuilder.loadTexts: dcxFPDFan3Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan3Fail.setDescription('Fan 3rd from the front failed')
dcxFPDFan3FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 8))
if mibBuilder.loadTexts: dcxFPDFan3FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan3FailClr.setDescription('Fan 3rd from the front is working')
dcxFPDFan4Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 9))
if mibBuilder.loadTexts: dcxFPDFan4Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan4Fail.setDescription('Fan 4th from the front failed')
dcxFPDFan4FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 10))
if mibBuilder.loadTexts: dcxFPDFan4FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan4FailClr.setDescription('Fan 4th from the front is working')
dcxFPDFan5Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 11))
if mibBuilder.loadTexts: dcxFPDFan5Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan5Fail.setDescription('Fan 5th from the front failed')
dcxFPDFan5FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 12))
if mibBuilder.loadTexts: dcxFPDFan5FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan5FailClr.setDescription('Fan 5th from the front is working')
dcxFPDFan6Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 13))
if mibBuilder.loadTexts: dcxFPDFan6Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan6Fail.setDescription('Fan nearest the back of the box failed')
dcxFPDFan6FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 14))
if mibBuilder.loadTexts: dcxFPDFan6FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDFan6FailClr.setDescription('Fan nearest the back of the box is working')
dcxFPDPwr1Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 15))
if mibBuilder.loadTexts: dcxFPDPwr1Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPwr1Fail.setDescription('Rightmost power supply failed')
dcxFPDPwr1FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 16))
if mibBuilder.loadTexts: dcxFPDPwr1FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPwr1FailClr.setDescription('Rightmost power supply is working')
dcxFPDPwr2Fail = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 17))
if mibBuilder.loadTexts: dcxFPDPwr2Fail.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPwr2Fail.setDescription('Leftmost power supply failed')
dcxFPDPwr2FailClr = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 18))
if mibBuilder.loadTexts: dcxFPDPwr2FailClr.setStatus('current')
if mibBuilder.loadTexts: dcxFPDPwr2FailClr.setDescription('Leftmost power supply is working')
dcxFPDTempOkay = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 19))
if mibBuilder.loadTexts: dcxFPDTempOkay.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTempOkay.setDescription('System temperature is OK')
dcxFPDTempBad = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 20))
if mibBuilder.loadTexts: dcxFPDTempBad.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTempBad.setDescription('System temperature is too hot!')
dcxFPDTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 3, 21))
if mibBuilder.loadTexts: dcxFPDTempCritical.setStatus('current')
if mibBuilder.loadTexts: dcxFPDTempCritical.setDescription('System temperature is critical!!!, CMTS will shut itself down!!!!')
dcxFPDConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4))
dcxFPDCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 1))
dcxFPDGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2))
dcxFPDCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 1, 1)).setObjects(("ARRIS-C3-FPD-MIB", "dcxFPDMsgGroup"), ("ARRIS-C3-FPD-MIB", "dcxFPDControlConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcxFPDCompliance = dcxFPDCompliance.setStatus('current')
if mibBuilder.loadTexts: dcxFPDCompliance.setDescription('The compliance statement for devices that implement Arris C3\n        compliant FPD features')
dcxFPDMsgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2, 1)).setObjects(("ARRIS-C3-FPD-MIB", "dcxFPDMsgString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcxFPDMsgGroup = dcxFPDMsgGroup.setStatus('current')
if mibBuilder.loadTexts: dcxFPDMsgGroup.setDescription('Arris C3 FPD message group')
dcxFPDControlConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 3, 1, 4, 2, 2)).setObjects(("ARRIS-C3-FPD-MIB", "dcxFPDAttachedStatus"), ("ARRIS-C3-FPD-MIB", "dcxFPDPowerStatus1"), ("ARRIS-C3-FPD-MIB", "dcxFPDPowerStatus2"), ("ARRIS-C3-FPD-MIB", "dcxFPDTemp1Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDTemp2Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDTemp3Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDTemp4Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan1Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan2Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan3Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan4Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan5Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFan6Status"), ("ARRIS-C3-FPD-MIB", "dcxFPDFanUpperLimit"), ("ARRIS-C3-FPD-MIB", "dcxFPDFanLowerLimit"), ("ARRIS-C3-FPD-MIB", "dcxFPDLCDContrast"), ("ARRIS-C3-FPD-MIB", "dcxFPDLedSetStatus"), ("ARRIS-C3-FPD-MIB", "dcxFPDHwRevision"), ("ARRIS-C3-FPD-MIB", "dcxFPDSwRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcxFPDControlConfGroup = dcxFPDControlConfGroup.setStatus('current')
if mibBuilder.loadTexts: dcxFPDControlConfGroup.setDescription('Arris C3 FPD Control group')
mibBuilder.exportSymbols("ARRIS-C3-FPD-MIB", dcxFPDFan6FailClr=dcxFPDFan6FailClr, dcxFPDTemp1Status=dcxFPDTemp1Status, dcxFPDFan5Fail=dcxFPDFan5Fail, cmtsC3FPDMIB=cmtsC3FPDMIB, dcxFPDTrapGroup=dcxFPDTrapGroup, dcxFPDFan2FailClr=dcxFPDFan2FailClr, dcxFPDAttached=dcxFPDAttached, dcxFPDGroups=dcxFPDGroups, dcxFPDFanUpperLimit=dcxFPDFanUpperLimit, dcxFPDTemp3Status=dcxFPDTemp3Status, dcxFPDFan6Status=dcxFPDFan6Status, dcxFPDFan4Status=dcxFPDFan4Status, dcxFPDLedSetStatus=dcxFPDLedSetStatus, dcxFPDFan1Fail=dcxFPDFan1Fail, dcxFPDPwr1FailClr=dcxFPDPwr1FailClr, dcxFPDPwr2FailClr=dcxFPDPwr2FailClr, dcxFPDCompliances=dcxFPDCompliances, dcxFPDFan3Status=dcxFPDFan3Status, dcxFPDMsgEntry=dcxFPDMsgEntry, dcxFPDPowerStatus2=dcxFPDPowerStatus2, dcxFPDFan1FailClr=dcxFPDFan1FailClr, dcxFPDTempCritical=dcxFPDTempCritical, dcxFPDFan2Status=dcxFPDFan2Status, dcxFPDPwr1Fail=dcxFPDPwr1Fail, dcxFPDMsgGroup=dcxFPDMsgGroup, dcxFPDFan1Status=dcxFPDFan1Status, dcxFPDFan5FailClr=dcxFPDFan5FailClr, dcxFPDControlGroup=dcxFPDControlGroup, dcxFPDLCDContrast=dcxFPDLCDContrast, dcxFPDPwr2Fail=dcxFPDPwr2Fail, dcxFPDTemp4Status=dcxFPDTemp4Status, dcxFPDFan3Fail=dcxFPDFan3Fail, dcxFPDFan6Fail=dcxFPDFan6Fail, dcxFPDCompliance=dcxFPDCompliance, dcxFPDPowerStatus1=dcxFPDPowerStatus1, dcxFPDObjects=dcxFPDObjects, dcxFPDHwRevision=dcxFPDHwRevision, dcxFPDMsgString=dcxFPDMsgString, dcxFPDFan4Fail=dcxFPDFan4Fail, dcxFPDFanLowerLimit=dcxFPDFanLowerLimit, dcxFPDMsgTable=dcxFPDMsgTable, dcxFPDTempOkay=dcxFPDTempOkay, dcxFPDMsgIndex=dcxFPDMsgIndex, dcxFPDTemp2Status=dcxFPDTemp2Status, dcxFPDControlConfGroup=dcxFPDControlConfGroup, dcxFPDDetached=dcxFPDDetached, dcxFPDAttachedStatus=dcxFPDAttachedStatus, dcxFPDFan5Status=dcxFPDFan5Status, dcxFPDTempBad=dcxFPDTempBad, dcxFPDFan2Fail=dcxFPDFan2Fail, dcxFPDSwRevision=dcxFPDSwRevision, dcxFPDFan3FailClr=dcxFPDFan3FailClr, PYSNMP_MODULE_ID=cmtsC3FPDMIB, dcxFPDConformance=dcxFPDConformance, dcxFPDFan4FailClr=dcxFPDFan4FailClr)
