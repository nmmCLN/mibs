#
# PySNMP MIB module IRT-TRANSMITTER-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-TRANSMITTER-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:07 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Bits, NotificationType, IpAddress, Unsigned32, MibIdentifier, Counter64, enterprises, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "NotificationType", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
irt = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831))
irt.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-07 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: irt.setRevisionsDescriptions(('change LocalRemote\n\t\t\t\tadd SFNMFN\n\t\t\t\t', 'Correction', 'Relocation of the TC-MIB from the standard OID area at IEC into the private OID area of the IRT ',))
if mibBuilder.loadTexts: irt.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: irt.setOrganization('IRT for WORKING-GROUP-TC-MIB')
if mibBuilder.loadTexts: irt.setContactInfo('Contact-info:\n\t\t\t\t\n\t\t\t\tAndreas Metz\n\t\t\t\t\n\t\t\t\tInstitut fuer Rundfunktechnik GmbH\n\t\t\t\tBroadcast Networks and Servers (SN)\n\t\t\t\t\n\t\t\t\tFloriansmuehlstr.60\n\t\t\t\t80939 Munich\n\t\t\t\tGermany\n\t\t\t\t\n\t\t\t\tPhone: +49 89 32399 325\n\t\t\t\tFax: +49 89 32399 354\n\t\t\t\t')
if mibBuilder.loadTexts: irt.setDescription('***************************************************\n\t\t\t\tDescription: IRT-TRANSMITTER-SMI-MIB General structure\n\t\t\t\t\n\t\t\t\tThis MIB defines the structure of a SNMP-Agent \n\t\t\t\tfor all kinds of reserve Transmitters\n\t\t\t\t\n\t\t\t\tPROJECT:    TC-MIB - TRANSMITTER-CONTROL-MIB\n\t\t\t\tOID:        1.3.6.1.4.1.19831\n\t\t\t\tFILE:       IRT-TRANSMITTER-SMI-MIB.*\n\t\t\t\tAUTHOR:     Ludmilla Leidag and Andreas Metz\n\t\t\t\t            for WORKING-GROUP-TC-MIB \n\t\t\t\t\n\t\t\t\t  \n\t\t\t\t***************************************************')
class SelectManualAuto(TextualConvention, Integer32):
    description = 'Description. Auto/Manual selection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("manual", 1), ("automatic", 2))

class SelectOnOff(TextualConvention, Integer32):
    description = 'Description. On/Off selection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("on", 1), ("off", 2))

class Input1Input2(TextualConvention, Integer32):
    description = 'Description.Input1/Input2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("input1", 1), ("input2", 2))

class OkNotOk(TextualConvention, Integer32):
    description = 'Description.OK/NotOK'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ok", 1), ("notok", 2))

class FaultOK(TextualConvention, Integer32):
    description = 'Description.Fault/OK'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fault", 1), ("ok", 2))

class WarningOK(TextualConvention, Integer32):
    description = 'Description.Warning/OK'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("warning", 1), ("ok", 2))

class LocalRemote(TextualConvention, Integer32):
    description = 'Description.Local/Remote'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("local", 1), ("remote", 2))

class MuteOk(TextualConvention, Integer32):
    description = 'Description. Mute/OK'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("mute", 1), ("ok", 2))

class ReadyNotReady(TextualConvention, Integer32):
    description = 'Description. Ready/Not ready'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ready", 1), ("notready", 2))

class ExecutedNotExecuted(TextualConvention, Integer32):
    description = 'Description. Executed/Not Executed'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("executed", 1), ("notexecuted", 2))

class PresentNotPresent(TextualConvention, Integer32):
    description = 'Description. Present/NotPresent'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("present", 1), ("notpresent", 2))

class SFNMFN(TextualConvention, Integer32):
    description = 'Description: SFN/MFN Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("sfn", 1), ("mfn", 2))

broadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1))
transmitter = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1))
dvbT = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1))
dab = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 2))
fm = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 3))
drm = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 4))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 7))
mibBuilder.exportSymbols("IRT-TRANSMITTER-SMI-MIB", OkNotOk=OkNotOk, transmitter=transmitter, Input1Input2=Input1Input2, ReadyNotReady=ReadyNotReady, dab=dab, PYSNMP_MODULE_ID=irt, broadcast=broadcast, FaultOK=FaultOK, LocalRemote=LocalRemote, irt=irt, SFNMFN=SFNMFN, MuteOk=MuteOk, SelectOnOff=SelectOnOff, WarningOK=WarningOK, PresentNotPresent=PresentNotPresent, dvbT=dvbT, common=common, SelectManualAuto=SelectManualAuto, ExecutedNotExecuted=ExecutedNotExecuted, fm=fm, drm=drm)
