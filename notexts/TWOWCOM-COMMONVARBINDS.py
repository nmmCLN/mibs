#
# PySNMP MIB module TWOWCOM-COMMONVARBINDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-COMMONVARBINDS
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:08 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, NotificationType, MibIdentifier, Integer32, Counter64, Gauge32, Bits, ObjectIdentity, IpAddress, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "iso", "TimeTicks")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
twowcom, = mibBuilder.importSymbols("TWOWCOM-SMI", "twowcom")
commonVarbinds = ModuleIdentity((1, 3, 6, 1, 4, 1, 21529, 11, 1))
commonVarbinds.setRevisions(('2011-05-26 12:00', '2010-02-17 16:00', '2009-02-06 13:30', '2008-04-28 15:17', '2008-03-26 15:36', '2007-04-26 08:52', '2006-10-26 16:13',))
if mibBuilder.loadTexts: commonVarbinds.setLastUpdated('201105261200Z')
if mibBuilder.loadTexts: commonVarbinds.setOrganization('2wcom GmbH')
class Integer32d(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class Integer32d1(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class Integer32d2(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class Integer32d3(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class Integer32h(TextualConvention, Integer32):
    reference = 'Interger32 hex'
    status = 'current'
    displayHint = 'x'

class ValidFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class ActiveNotActive(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notActive", 0), ("active", 1))

class SelectOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("on", 1), ("off", 2))

class FaultOK(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fault", 1), ("ok", 2))

class SelectYesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FloatString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d1dEE1a1d1d'

class Unsigned16x(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = '4x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

common = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 11))
commonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21529, 11, 1, 1)).setObjects(("TWOWCOM-COMMONVARBINDS", "eventTimeStamp"), ("TWOWCOM-COMMONVARBINDS", "eventPriority"), ("TWOWCOM-COMMONVARBINDS", "eventCounter"), ("TWOWCOM-COMMONVARBINDS", "mibRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    commonGroup = commonGroup.setStatus('current')
eventTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
eventPriority = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPriority.setStatus('current')
eventCounter = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCounter.setStatus('current')
mibRelease = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibRelease.setStatus('current')
mibBuilder.exportSymbols("TWOWCOM-COMMONVARBINDS", eventCounter=eventCounter, Integer32d2=Integer32d2, SelectOnOff=SelectOnOff, Integer32h=Integer32h, Unsigned16x=Unsigned16x, FloatString=FloatString, mibRelease=mibRelease, eventTimeStamp=eventTimeStamp, common=common, PYSNMP_MODULE_ID=commonVarbinds, Integer32d1=Integer32d1, FaultOK=FaultOK, ActiveNotActive=ActiveNotActive, ValidFlag=ValidFlag, commonGroup=commonGroup, commonVarbinds=commonVarbinds, eventPriority=eventPriority, SelectYesNo=SelectYesNo, Integer32d3=Integer32d3, Integer32d=Integer32d)
