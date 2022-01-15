#
# PySNMP MIB module IEEE8021-ST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-ST-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ieee8021STMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 30))
ieee8021STMib.setRevisions(('2018-06-21 00:00', '2016-08-15 00:00', '2016-02-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021STMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2017 revision.\n        Cross references updated and corrected.', 'Revised to include Set-And-Hold-MAC and\n        Set-And-Release-MAC in the description of\n        ieee8021STAdminControlList and\n        ieee8021STOperControlList.\n        Published as part of IEEE Std 802.1Qbu.', 'Initial version published as part of IEEE Std 802.1Qbv.',))
if mibBuilder.loadTexts: ieee8021STMib.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: ieee8021STMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021STMib.setContactInfo('  WG-URL: http://www.ieee802.org/1/\n         WG-EMail: stds-802-1-L@ieee.org\n\n          Contact: IEEE 802.1 Working Group Chair\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   Piscataway\n                   NJ 08854\n                   USA\n           E-mail: stds-802-1-L@ieee.org')
if mibBuilder.loadTexts: ieee8021STMib.setDescription('The Bridge MIB module for managing devices that support\n        the Scheduled Traffic Enhancements\n        for IEEE 802.1Q Bridges.\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1Q.\n\n        Copyright (C) IEEE (2018).\n        This version of this MIB module is part of IEEE Std 802.1Q;\n        see the draft itself for full legal notices.')
class IEEE8021STTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.29.1'
    description = 'A traffic class value.\n        This is the numerical value associated with a traffic\n        class in a Bridge. Larger values are associated with\n        higher priority traffic classes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021STPTPtimeValue(TextualConvention, OctetString):
    reference = '8.6.8.4, 8.6.9.4, 12.29.1'
    description = 'A PTPtime value, represented as a 48-bit unsigned integer \n        number of seconds and a 32-bit unsigned integer number of\n        nanoseconds.\n        The first 6 octets represent the number of seconds: the \n        first octet is the most significant\n        octet of the 48-bit seconds value and the sixth octet\n        is the least significant octet of the seconds value.\n        The remaining octets, 7 through 10,  represent the \n        number of nanoseconds: the seventh octet \n        is the most significant octet of the 32-bit nanoseconds\n        value and the tenth octet is the \n        least significant octet of the nanoseconds value.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

ieee8021STNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 0))
ieee8021STObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1))
ieee8021STConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2))
ieee8021STMaxSDUSubtree = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1, 1))
ieee8021STParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 1, 2))
ieee8021STMaxSDUTable = MibTable((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021STMaxSDUTable.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STMaxSDUTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021STMaxSDUTable.setDescription('A table containing a set of max SDU \n        parameters, one for each traffic class.\n        All writeable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021STMaxSDUEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-ST-MIB", "ieee8021STTrafficClass"))
if mibBuilder.loadTexts: ieee8021STMaxSDUEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021STMaxSDUEntry.setDescription('A list of objects containing Max SDU size \n        for each traffic class supported by the Port.')
ieee8021STTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 1), IEEE8021STTrafficClassValue())
if mibBuilder.loadTexts: ieee8021STTrafficClass.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021STTrafficClass.setDescription('The traffic class number associated with the row of\n        the table.\n\n        A row in this table is created for each traffic class\n        that is supported by the Port')
ieee8021STMaxSDU = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 2), Unsigned32()).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STMaxSDU.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STMaxSDU.setStatus('current')
if mibBuilder.loadTexts: ieee8021STMaxSDU.setDescription('The value of the MaxSDU parameter for the traffic class.\n        This value is represented as an unsigned integer. A value\n        of 0 is interpreted as the max SDU size supported by\n        the underlying MAC.\n\n        The default value of the MaxSDU parameter is 0.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021TransmissionOverrun = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TransmissionOverrun.setReference('8.6.8.4, 8.6.9.4, 12.29.1, 12.29.1.1.2')
if mibBuilder.loadTexts: ieee8021TransmissionOverrun.setStatus('current')
if mibBuilder.loadTexts: ieee8021TransmissionOverrun.setDescription('A counter of transmission overrun events, where\n        a PDU is still being transmitted by a MAC at the\n        time when the transmission gate for the queue closed.')
ieee8021STParametersTable = MibTable((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021STParametersTable.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STParametersTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021STParametersTable.setDescription('A table that contains the per-port manageable parameters for \n        traffic scheduling.\n\n        For a given Port, a row in the table exists.\n\n        All writable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021STParametersEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021STParametersEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021STParametersEntry.setDescription('A list of objects that contains the manageable parameters for \n        traffic scheduling for a port.')
ieee8021STGateEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STGateEnabled.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STGateEnabled.setStatus('current')
if mibBuilder.loadTexts: ieee8021STGateEnabled.setDescription('The GateEnabled parameter determines whether traffic scheduling\n        is active (true) or inactive (false).\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STAdminGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminGateStates.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminGateStates.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminGateStates.setDescription('The administrative value of the GateStates parameter for the Port.\n        The bits of the octet represent the gate states for the \n        corresponding traffic classes; the MS bit corresponds to traffic class 7,\n        the LS bit to traffic class 0. A bit value of 0 indicates closed; a \n        bit value of 1 indicates open.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperGateStates = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperGateStates.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperGateStates.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperGateStates.setDescription('The operational value of the GateStates parameter for the Port.\n        The bits of the octet represent the gate states for the \n        corresponding traffic classes; the MS bit corresponds to traffic class 7,\n        the LS bit to traffic class 0. A bit value of 0 indicates closed; a \n        bit value of 1 indicates open.')
ieee8021STAdminControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminControlListLength.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminControlListLength.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminControlListLength.setDescription('The administrative value of the ListMax parameter for the Port.\n        The integer value indicates the number of entries (TLVs) in the\n        AdminControlList.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperControlListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperControlListLength.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperControlListLength.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperControlListLength.setDescription('The operational value of the ListMax parameter for the Port.\n        The integer value indicates the number of entries (TLVs) in the\n        OperControlList.')
ieee8021STAdminControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminControlList.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminControlList.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminControlList.setDescription('The administrative value of the ControlList parameter for the Port.\n        The octet string value represents the contents of the control list as\n        an ordered list of entries, each encoded as a TLV, as follows.\n        The first octet  of each TLV is interpreted as an\n        unsigned integer representing a gate operation name:\n            0: SetGateStates\n            1: Set-And-Hold-MAC\n            2: Set-And-Release-MAC\n            3-255: Reserved for future gate operations\n            \n        The second octet of the TLV is the length field, \n        interpreted as an unsigned integer, indicating the number of\n        octets of the value that follows the length. A length of\n        zero indicates that there is no value \n        (i.e., the gate operation has no parameters).\n        \n        The third through (3 + length -1)th octets encode the \n        parameters of the gate operation, in the order that they \n        appear in the definition of the operation\n        in Table 8-6. Two parameter types are currently defined:\n        \n        - GateState:\n            A GateState parameter is encoded in a single octet.\n            The bits of the octet represent the gate states for the \n            corresponding traffic classes; the MS bit corresponds\n            to traffic class 7,\n            the LS bit to traffic class 0. A bit value of 0 indicates\n            closed; a bit value of 1 indicates open.\n            \n        - TimeInterval: \n            A TimeInterval is encoded in 4 octets as a 32-bit \n            unsigned integer, representing a number of nanoseconds.\n            The first octet encodes the most significant 8 bits of the \n            integer, and the fourth octet encodes the least \n            significant 8 bits.\n        \n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperControlList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperControlList.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperControlList.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperControlList.setDescription('The operational value of the ListMax parameter for the Port.\n        The octet string value represents the contents of the control list as\n        an ordered list of TLVs, as follows.\n        The first octet  of each TLV is interpreted as a gate operation name:\n            0: SetGateStates\n            1: Set-And-Hold-MAC\n            2: Set-And-Release-MAC\n            3-255: Reserved for future gate operations\n            \n        The second octet of the TLV is the length field, \n        interpreted as an unsigned integer,\n        indicating the number of octets of the value that follows\n        the length. A length of zero indicates that there is no value \n        (i.e., the gate operation has no parameters).\n        \n        The third through (3 + length -1)th octets encode the \n        parameters of the gate operation, in the order that they \n        appear in the definition of the operation\n        in Table 8-6. Two parameter types are currently defined:\n        \n        - GateState:\n            A GateState parameter is encoded in a single octet.\n            The bits of the octet represent the gate states for the \n            corresponding traffic classes; the MS bit corresponds to\n            traffic class 7, the LS bit to traffic class 0. \n            A bit value of 0 indicates closed; a \n            bit value of 1 indicates open.\n            \n        - TimeInterval: \n            A TimeInterval is encoded in 4 octets as a 32-bit \n            unsigned integer, representing\n            a number of nanoseconds. The first octet encodes the\n            most significant 8 bits of the integer, and the fourth\n            octet encodes the least significant 8 bits.')
ieee8021STAdminCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeNumerator.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeNumerator.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeNumerator.setDescription('The administrative value of the numerator of the CycleTime\n        parameter for the Port.\n        The numerator and denominator together represent the cycle time as\n        a rational number of seconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STAdminCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeDenominator.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeDenominator.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeDenominator.setDescription('The administrative value of the denominator of the \n        CycleTime parameter for the Port.\n        The numerator and denominator together represent the cycle time as\n        a rational number of seconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperCycleTimeNumerator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeNumerator.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeNumerator.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeNumerator.setDescription('The operational value of the numerator of the \n        CycleTime parameter for the Port.\n        The numerator and denominator together represent the cycle\n        time as a rational number of seconds.')
ieee8021STOperCycleTimeDenominator = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeDenominator.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeDenominator.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeDenominator.setDescription('The operational value of the denominator of the \n        CycleTime parameter for the Port.\n        The numerator and denominator together represent the \n        cycle time as a rational number of seconds.')
ieee8021STAdminCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 12), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeExtension.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeExtension.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminCycleTimeExtension.setDescription('The administrative value of the CycleTimeExtension \n        parameter for the Port. \n        The value is an unsigned integer number of nanoseconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperCycleTimeExtension = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 13), Unsigned32()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperCycleTimeExtension.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeExtension.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperCycleTimeExtension.setDescription('The operational value of the CycleTimeExtension parameter for the Port.\n        The value is an unsigned integer number of nanoseconds.')
ieee8021STAdminBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 14), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STAdminBaseTime.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STAdminBaseTime.setStatus('current')
if mibBuilder.loadTexts: ieee8021STAdminBaseTime.setDescription('The administrative value of the BaseTime parameter for the Port.\n        The value is a representation of a PTPtime value, \n        consisting of a 48-bit integer\n        number of seconds and a 32-bit integer number of nanoseconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STOperBaseTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 15), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STOperBaseTime.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STOperBaseTime.setStatus('current')
if mibBuilder.loadTexts: ieee8021STOperBaseTime.setDescription('The operationsl value of the BaseTime parameter for the Port.\n        The value is a representation of a PTPtime value, \n        consisting of a 48-bit integer\n        number of seconds and a 32-bit integer number of nanoseconds.')
ieee8021STConfigChange = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021STConfigChange.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STConfigChange.setStatus('current')
if mibBuilder.loadTexts: ieee8021STConfigChange.setDescription('The ConfigChange parameter signals the start of a \n        configuration change\n        when it is set to TRUE. This should only be done\n        when the various administrative parameters\n        are all set to appropriate values.')
ieee8021STConfigChangeTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 17), IEEE8021STPTPtimeValue()).setUnits('PTP time').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigChangeTime.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STConfigChangeTime.setStatus('current')
if mibBuilder.loadTexts: ieee8021STConfigChangeTime.setDescription('The PTPtime at which the next config change is scheduled to occur.\n        The value is a representation of a PTPtime value, \n        consisting of a 48-bit integer\n        number of seconds and a 32-bit integer number of nanoseconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STTickGranularity = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STTickGranularity.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STTickGranularity.setStatus('current')
if mibBuilder.loadTexts: ieee8021STTickGranularity.setDescription('The granularity of the cycle time clock, represented as an\n        unsigned number of tenths of nanoseconds.\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021STCurrentTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 19), IEEE8021STPTPtimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STCurrentTime.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STCurrentTime.setStatus('current')
if mibBuilder.loadTexts: ieee8021STCurrentTime.setDescription('The current time, in PTPtime, as maintained by the local system.\n        The value is a representation of a PTPtime value, \n        consisting of a 48-bit integer\n        number of seconds and a 32-bit integer number of nanoseconds.')
ieee8021STConfigPending = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigPending.setReference('8.6.8.4, 8.6.9.4, 12.29.1')
if mibBuilder.loadTexts: ieee8021STConfigPending.setStatus('current')
if mibBuilder.loadTexts: ieee8021STConfigPending.setDescription('The value of the ConfigPending state machine variable.\n        The value is TRUE if a configuration change is in progress\n        but has not yet completed.')
ieee8021STConfigChangeError = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STConfigChangeError.setReference('8.6.8.4, 8.6.9.3, 8.6.9.1.1, 12.29.1')
if mibBuilder.loadTexts: ieee8021STConfigChangeError.setStatus('current')
if mibBuilder.loadTexts: ieee8021STConfigChangeError.setDescription('A counter of the number of times that a re-configuration\n        of the traffic schedule has been requested with the old\n        schedule still running and the requested base time was\n        in the past.')
ieee8021STSupportedListMax = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021STSupportedListMax.setReference('12.29.1.5')
if mibBuilder.loadTexts: ieee8021STSupportedListMax.setStatus('current')
if mibBuilder.loadTexts: ieee8021STSupportedListMax.setDescription('The maximum value supported by this Port of the \n        AdminControlListLength and OperControlListLength\n        parameters.')
ieee8021STCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2, 1))
ieee8021STGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 30, 2, 2))
ieee8021STObjectsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 30, 2, 2, 1)).setObjects(("IEEE8021-ST-MIB", "ieee8021STMaxSDU"), ("IEEE8021-ST-MIB", "ieee8021TransmissionOverrun"), ("IEEE8021-ST-MIB", "ieee8021STGateEnabled"), ("IEEE8021-ST-MIB", "ieee8021STAdminGateStates"), ("IEEE8021-ST-MIB", "ieee8021STOperGateStates"), ("IEEE8021-ST-MIB", "ieee8021STAdminControlListLength"), ("IEEE8021-ST-MIB", "ieee8021STOperControlListLength"), ("IEEE8021-ST-MIB", "ieee8021STAdminControlList"), ("IEEE8021-ST-MIB", "ieee8021STOperControlList"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeNumerator"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeDenominator"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeNumerator"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeDenominator"), ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeExtension"), ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeExtension"), ("IEEE8021-ST-MIB", "ieee8021STAdminBaseTime"), ("IEEE8021-ST-MIB", "ieee8021STOperBaseTime"), ("IEEE8021-ST-MIB", "ieee8021STConfigChange"), ("IEEE8021-ST-MIB", "ieee8021STConfigChangeTime"), ("IEEE8021-ST-MIB", "ieee8021STTickGranularity"), ("IEEE8021-ST-MIB", "ieee8021STCurrentTime"), ("IEEE8021-ST-MIB", "ieee8021STConfigPending"), ("IEEE8021-ST-MIB", "ieee8021STConfigChangeError"), ("IEEE8021-ST-MIB", "ieee8021STSupportedListMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021STObjectsGroup = ieee8021STObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021STObjectsGroup.setDescription('Objects that allow management of scheduled traffic.')
ieee8021STCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 30, 2, 1, 1)).setObjects(("IEEE8021-ST-MIB", "ieee8021STObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021STCompliance = ieee8021STCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021STCompliance.setDescription('The compliance statement for devices supporting \n        scheduled traffic. \n\n        Support of the objects defined in this MIB module\n        also requires support of the IEEE8021-BRIDGE-MIB; the\n        provisions of 17.3.2 apply to implementations claiming\n        support of this MIB. ')
mibBuilder.exportSymbols("IEEE8021-ST-MIB", ieee8021STMib=ieee8021STMib, ieee8021STParametersTable=ieee8021STParametersTable, ieee8021STConfigChange=ieee8021STConfigChange, ieee8021STTickGranularity=ieee8021STTickGranularity, IEEE8021STTrafficClassValue=IEEE8021STTrafficClassValue, ieee8021STGroups=ieee8021STGroups, ieee8021STObjects=ieee8021STObjects, ieee8021STOperCycleTimeDenominator=ieee8021STOperCycleTimeDenominator, ieee8021STAdminCycleTimeDenominator=ieee8021STAdminCycleTimeDenominator, ieee8021STConfigChangeTime=ieee8021STConfigChangeTime, ieee8021STCompliance=ieee8021STCompliance, IEEE8021STPTPtimeValue=IEEE8021STPTPtimeValue, ieee8021STParametersEntry=ieee8021STParametersEntry, ieee8021STCurrentTime=ieee8021STCurrentTime, ieee8021STSupportedListMax=ieee8021STSupportedListMax, PYSNMP_MODULE_ID=ieee8021STMib, ieee8021STMaxSDU=ieee8021STMaxSDU, ieee8021STOperControlListLength=ieee8021STOperControlListLength, ieee8021STAdminControlListLength=ieee8021STAdminControlListLength, ieee8021STConfigChangeError=ieee8021STConfigChangeError, ieee8021STOperCycleTimeExtension=ieee8021STOperCycleTimeExtension, ieee8021STOperBaseTime=ieee8021STOperBaseTime, ieee8021STOperGateStates=ieee8021STOperGateStates, ieee8021STMaxSDUEntry=ieee8021STMaxSDUEntry, ieee8021STMaxSDUSubtree=ieee8021STMaxSDUSubtree, ieee8021STAdminCycleTimeExtension=ieee8021STAdminCycleTimeExtension, ieee8021STTrafficClass=ieee8021STTrafficClass, ieee8021STMaxSDUTable=ieee8021STMaxSDUTable, ieee8021STParameters=ieee8021STParameters, ieee8021STConformance=ieee8021STConformance, ieee8021TransmissionOverrun=ieee8021TransmissionOverrun, ieee8021STAdminCycleTimeNumerator=ieee8021STAdminCycleTimeNumerator, ieee8021STNotifications=ieee8021STNotifications, ieee8021STCompliances=ieee8021STCompliances, ieee8021STAdminGateStates=ieee8021STAdminGateStates, ieee8021STGateEnabled=ieee8021STGateEnabled, ieee8021STAdminBaseTime=ieee8021STAdminBaseTime, ieee8021STAdminControlList=ieee8021STAdminControlList, ieee8021STConfigPending=ieee8021STConfigPending, ieee8021STObjectsGroup=ieee8021STObjectsGroup, ieee8021STOperCycleTimeNumerator=ieee8021STOperCycleTimeNumerator, ieee8021STOperControlList=ieee8021STOperControlList)
