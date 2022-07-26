#
# PySNMP MIB module SL-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ENTITY-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:39 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, NotificationType, iso, MibIdentifier, ModuleIdentity, Counter32, mib_2, TimeTicks, IpAddress, Integer32, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "NotificationType", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "mib-2", "TimeTicks", "IpAddress", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity")
TDomain, RowStatus, PhysAddress, TAddress, TextualConvention, AutonomousType, TimeStamp, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "RowStatus", "PhysAddress", "TAddress", "TextualConvention", "AutonomousType", "TimeStamp", "TruthValue", "DisplayString")
slmEntity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6))
if mibBuilder.loadTexts: slmEntity.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slmEntity.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slmEntity.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slmEntity.setDescription('The MIB module for representing multiple physical\n\t\tentities supported by a single SNMP agent. The MIB\n\t\tis based on the standard RFC-2737 entity-mib.')
class PhysicalIndex(TextualConvention, Integer32):
    description = 'An arbitrary value which uniquely identifies the physical\n            entity.  The value should be a small positive integer; index\n            values for different physical entities are not necessarily\n            contiguous.\n            The index 0 is for the Shelf.\n            The indices 1..100 are for the Cards.\n            The indices 101..102 are reserved for the Power-Supply.\n            The indices 103..110 are reserved for the Fans.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PhysicalClass(TextualConvention, Integer32):
    description = "An enumerated value which provides an indication of the\n            general hardware type of a particular physical entity.\n            There are no restrictions as to the number of\n            slEntPhysicalEntries of each slEntPhysicalClass, which must be\n            instantiated by an agent.\n\n            The enumeration 'other' is applicable if the physical entity\n            class is known, but does not match any of the supported\n            values.\n\n            The enumeration 'unknown' is applicable if the physical\n            entity class is unknown to the agent.\n\n            The enumeration 'chassis' is applicable if the physical\n            entity class is an overall container for networking\n            equipment.  Any class of physical entity except a stack may\n            be contained within a chassis, and a chassis may only be\n            contained within a stack.\n\n            The enumeration 'backplane' is applicable if the physical\n            entity class is some sort of device for aggregating and\n            forwarding networking traffic, such as a shared backplane in\n            a modular ethernet switch.  Note that an agent may model a\n            backplane as a single physical entity, which is actually\n            implemented as multiple discrete physical components (within\n            a chassis or stack).\n\n            The enumeration 'container' is applicable if the physical\n            entity class is capable of containing one or more removable\n            physical entities, possibly of different types. For example,\n            each (empty or full) slot in a chassis will be modeled as a\n            container. Note that all removable physical entities should\n            be modeled within a container entity, such as field-\n            replaceable modules, fans, or power supplies.  Note that all\n            known containers should be modeled by the agent, including\n            empty containers.\n\n            The enumeration 'powerSupply' is applicable if the physical\n            entity class is a power-supplying component.\n\n            The enumeration 'fan' is applicable if the physical entity\n            class is a fan or other heat-reduction component.\n\n            The enumeration 'sensor' is applicable if the physical\n            entity class is some sort of sensor, such as a temperature\n            sensor within a router chassis.\n\n            The enumeration 'module' is applicable if the physical\n            entity class is some sort of self-contained sub-system.  If\n            it is removable, then it should be modeled within a\n            container entity, otherwise it should be modeled directly\n            within another physical entity (e.g., a chassis or another\n            module).\n\n            The enumeration 'port' is applicable if the physical entity\n            class is some sort of networking port, capable of receiving\n            and/or transmitting networking traffic.\n\n            The enumeration 'stack' is applicable if the physical entity\n            class is some sort of super-container (possibly virtual),\n            intended to group together multiple chassis entities.  A\n            stack may be realized by a 'virtual' cable, a real\n            interconnect cable, attached to multiple chassis, or may in\n            fact be comprised of multiple interconnect cables. A stack\n            should not be modeled within any other physical entities,\n            but a stack may be contained within another stack.  Only\n            chassis entities should be contained within a stack."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11))

class PhysicalType(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the\n            general card type of a particular physical entity.\n            There are no restrictions as to the number of\n            slEntPhysicalEntries of each PhysicalType, which must be\n            instantiated by an agent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 14, 15, 16, 21, 100))
    namedValues = NamedValues(("powerModule", 1), ("fanModule", 2), ("switchModule", 3), ("edfaModule", 14), ("ocmModule", 15), ("otdrModule", 16), ("lc400G", 21), ("unknown", 100))

class CleiCode(DisplayString):
    reference = 'GR-383-CORE'
    description = 'COMMON LANGUAGE Equipment Code.\n            The CLEI code contains an intelligent \n            ten-character code that identifies the \n            telecommunications equipment.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

slEntityPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1))
slEntityNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 2))
slEntPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1), )
if mibBuilder.loadTexts: slEntPhysicalTable.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalTable.setDescription("This table contains one row per physical entity.  There is\n            always at least one row for an 'overall' physical entity.")
slEntPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1), ).setIndexNames((0, "SL-ENTITY-MIB", "slEntPhysicalIndex"))
if mibBuilder.loadTexts: slEntPhysicalEntry.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalEntry.setDescription('Information about a particular physical entity.')
slEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalIndex.setDescription('The Slot number of the entity.')
slEntPhysicalDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalDescr.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalDescr.setDescription("A textual description of physical entity.  This object\n            should contain a string which identifies the manufacturer's\n            name for the physical entity, and should be set to a\n            distinct value for each version or model of the physical\n            entity. \n            The actual value should be taken from the E2prom.")
slEntPhysicalClass = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 3), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalClass.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalClass.setDescription("An indication of the general hardware type of the physical\n            entity.\n\n            An agent should set this object to the standard enumeration\n            value which most accurately indicates the general class of\n            the physical entity, or the primary class if there is more\n            than one.\n\n            If no appropriate standard registration identifier exists\n            for this physical entity, then the value 'other(1)' is\n            returned. If the value is unknown by this agent, then the\n            value 'unknown(2)' is returned.")
slEntPhysicalHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalHardwareRev.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalHardwareRev.setDescription('The vendor-specific hardware revision string for the\n            physical entity.  The preferred value is the hardware\n            revision identifier actually printed on the component itself\n            (if present).\n\n            Note that if revision information is stored internally in a\n            non-printable (e.g., binary) format, then the agent must\n            convert such information to a printable format, in an\n            implementation-specific manner.\n\n            If no specific hardware revision string is associated with\n            the physical component, or this information is unknown to\n            the agent, then this object will contain a zero-length\n            string.')
slEntPhysicalFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalFirmwareRev.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalFirmwareRev.setDescription('The vendor-specific firmware revision string for the\n            physical entity (normally the boot-revision).\n\n            Note that if revision information is stored internally in a\n            non-printable (e.g., binary) format, then the agent must\n            convert such information to a printable format, in an\n            implementation-specific manner.\n\n            If no specific firmware programs are associated with the\n            physical component, or this information is unknown to the\n            agent, then this object will contain a zero-length string.')
slEntPhysicalSoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSoftwareRev.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSoftwareRev.setDescription('The vendor-specific software revision string for the\n            physical entity.\n\n            Note that if revision information is stored internally in a\n            non-printable (e.g., binary) format, then the agent must\n            convert such information to a printable format, in an\n            implementation-specific manner.\n\n            If no specific software programs are associated with the\n            physical component, or this information is unknown to the\n            agent, then this object will contain a zero-length string.')
slEntPhysicalSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSerialNum.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSerialNum.setDescription("The vendor-specific serial number string for the physical\n            entity.  The preferred value is the serial number string\n            actually printed on the component itself (if present).\n\n            On the first instantiation of an physical entity, the value\n            of slEntPhysicalSerialNum associated with that entity is set\n            to the correct vendor-assigned serial number, if this\n            information is available to the agent.  If a serial number\n            is unknown or non-existent, the slEntPhysicalSerialNum will be\n            set to a zero-length string instead.\n\n            Note that implementations which can correctly identify the\n            serial numbers of all installed physical entities do not\n            need to provide write access to the slEntPhysicalSerialNum\n            object. Agents which cannot provide non-volatile storage for\n            the slEntPhysicalSerialNum strings are not required to\n            implement write access for this object.\n\n            Not every physical component will have a serial number, or\n            even need one.  Physical entities for which the associated\n            value of the slEntPhysicalIsFRU object is equal to 'false(2)'\n            (e.g., the repeater ports within a repeater module), do not\n            need their own unique serial number. An agent does not have\n            to provide write access for such entities, and may return a\n            zero-length string.\n\n            If write access is implemented for an instance of\n            slEntPhysicalSerialNum, and a value is written into the\n            instance, the agent must retain the supplied value in the\n            slEntPhysicalSerialNum instance associated with the same\n            physical entity for as long as that entity remains\n            instantiated. This includes instantiations across all re-\n            initializations/reboots of the network management system,\n            including those which result in a change of the physical\n            entity's slEntPhysicalIndex value.")
slEntPhysicalProtectionEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 8), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalProtectionEntity.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalProtectionEntity.setDescription("The value of slEntPhysicalIndex for the physical entity which\n            'protects' this physical entity.  A value of zero indicates\n            this physical entity has no protecting physical\n            entity.\n            This object is not applicable should the protection be done\n            on a per-port basis.")
slEntPhysicalProtectState = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protecting", 2), ("noProtection", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalProtectState.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalProtectState.setDescription('The protection state of physical entity.\n            This object is not applicable should the protection be done\n            on a per-port basis.\n            In the case of Switch protection the following logic should be used:\n            1. If there is only one card is present - noProtection(3)\n            2. If the standby card is not ready - the active card\n               should have the value noProtection(3), and the standby\n               card should have the value protecting(2)\n            3. If the protecting card is ready - the active card should\n               have the value working(1) and the standby card should have\n               the value protecting(2)')
slEntPhysicalProtectMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lock", 1), ("force", 2), ("automatic", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalProtectMode.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalProtectMode.setDescription('The protection mode of physical entity.\n            The default value is automatic(3)\n            This object is not applicable should the protection be done\n            on a per-port basis.')
slEntPhysicalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalStatus.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalStatus.setDescription('The physical entity status bitmap:\n        \t1 - Card is removed from the slot           \n          \t2 - Communication Fault \n          \t4 - Major alarm inherited from the ports   \n          \t8 - Card or port HW failure\n           16 - An internal SW failure detected\n\t\t   32 - SW version mismatch detected\n           64 - Power A Failure\n          128 - Power B Failure\n          256 - HW version mismatch detected\n          512 - Minor alarm inherited from the ports')
slEntPhysicalFailureDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalFailureDescription.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalFailureDescription.setDescription('Text that describes the last entity failure.')
slEntPhysicalAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("warmBoot", 4), ("coldBoot", 5), ("hotBoot", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalAdminStatus.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalAdminStatus.setDescription('The desired state of the interface.  The testing(3)\n               state indicates that no operational packets can be\n               passed.  When a managed system initializes, all\n               interfaces start with ifAdminStatus in the down(2)\n               state.  As a result of either explicit management\n               action or per configuration information retained by\n               the managed system, ifAdminStatus is then changed to\n               either the up(1) or testing(3) states (or remains in\n               the down(2) state).\n               State warmBoot(4) cause the card a Warm Start.\n               The state coldBoot(5)has two meanings. If the card is present\n               it means to reinitialize it with the factory defaults. This\n               is equivalent to Cold Start. \n               Setting the object to the value hotBoot(7) cause the\n               card to reboot in a non service affecting manner.\n               If the card is not present it means that the former\n               configuration of this slot is not longer kept in the\n               system. In this case the slot is ready for insertion of\n               a new card of any type.')
slEntPhysicalOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 6))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("notPresent", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalOperStatus.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalOperStatus.setDescription('The current operational state of the interface.  \n               If slEntPhysicalAdminStatus is down(2) then\n               slEntPhysicalOperStatus should be down(2). \n               If slEntPhysicalAdminStatus is changed to up(1) \n               then slEntPhysicalOperStatus should change to\n               up(1) if the interface is ready to transmit and\n               receive network traffic It should remain in \n               the down(2) state if and only if there is a \n               fault that prevents it from going to the up(1) state; it should remain in the\n               notPresent(6) state if the interface has missing\n               (typically, hardware) components.')
slEntPhysicalSysUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 19), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysUptime.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSysUptime.setDescription('The number of timer ticks since the last reboot of the module.')
slEntPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 20), PhysicalType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalType.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalType.setDescription('The type of the physical module.')
slEntPhysicalCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 21), CleiCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalCleiCode.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalCleiCode.setDescription('The Clei Code resides in the SEEP of each card.')
slEntPhysicalPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 22), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalPartNumber.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalPartNumber.setDescription('The card part number. This is a string of upto 12 characters.')
slEntPhysicalOemSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 23), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalOemSerialNum.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalOemSerialNum.setDescription("The oem-specific serial number string for the physical\n            entity.  The preferred value is the serial number string\n            actually printed on the component itself (if present).\n\n            On the first instantiation of an physical entity, the value\n            of slEntPhysicalSerialNum associated with that entity is set\n            to the correct vendor-assigned serial number, if this\n            information is available to the agent.  If a serial number\n            is unknown or non-existent, the slEntPhysicalSerialNum will be\n            set to a zero-length string instead.\n\n            Note that implementations which can correctly identify the\n            serial numbers of all installed physical entities do not\n            need to provide write access to the slEntPhysicalSerialNum\n            object. Agents which cannot provide non-volatile storage for\n            the slEntPhysicalSerialNum strings are not required to\n            implement write access for this object.\n\n            Not every physical component will have a serial number, or\n            even need one.  Physical entities for which the associated\n            value of the slEntPhysicalIsFRU object is equal to 'false(2)'\n            (e.g., the repeater ports within a repeater module), do not\n            need their own unique serial number. An agent does not have\n            to provide write access for such entities, and may return a\n            zero-length string.\n\n            If write access is implemented for an instance of\n            slEntPhysicalSerialNum, and a value is written into the\n            instance, the agent must retain the supplied value in the\n            slEntPhysicalSerialNum instance associated with the same\n            physical entity for as long as that entity remains\n            instantiated. This includes instantiations across all re-\n            initializations/reboots of the network management system,\n            including those which result in a change of the physical\n            entity's slEntPhysicalIndex value.")
slEntPhysicalProductionDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 24), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalProductionDate.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalProductionDate.setDescription('The entity production date in the format YYYY-WW.')
slEntPhysicalSysTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysTemp.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSysTemp.setDescription('Internally measured module temperature. The value 0 means -128 Celsuis. \n\t\tAn increment on one is equivalent to 1/256 degree,\n\t\tyielding a total range of -128 to +128 Celsius.')
slEntPhysicalSysAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 26), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEntPhysicalSysAlias.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSysAlias.setDescription('The module alias as given by the user.')
slEntPhysicalSysSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 6, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEntPhysicalSysSubType.setStatus('current')
if mibBuilder.loadTexts: slEntPhysicalSysSubType.setDescription('The subtype of the physical module.\n        The possibel values of this object are drived from the value of slEntPhysicalType.')
mibBuilder.exportSymbols("SL-ENTITY-MIB", slEntPhysicalSysUptime=slEntPhysicalSysUptime, slEntPhysicalOperStatus=slEntPhysicalOperStatus, slEntPhysicalSysSubType=slEntPhysicalSysSubType, slEntPhysicalAdminStatus=slEntPhysicalAdminStatus, slEntPhysicalProtectState=slEntPhysicalProtectState, CleiCode=CleiCode, slEntPhysicalSoftwareRev=slEntPhysicalSoftwareRev, slEntPhysicalFailureDescription=slEntPhysicalFailureDescription, slEntPhysicalSysAlias=slEntPhysicalSysAlias, PhysicalClass=PhysicalClass, slEntPhysicalProtectionEntity=slEntPhysicalProtectionEntity, slEntPhysicalTable=slEntPhysicalTable, slEntPhysicalClass=slEntPhysicalClass, slEntPhysicalEntry=slEntPhysicalEntry, slEntityNotification=slEntityNotification, PhysicalType=PhysicalType, slEntPhysicalStatus=slEntPhysicalStatus, slEntPhysicalHardwareRev=slEntPhysicalHardwareRev, slEntPhysicalOemSerialNum=slEntPhysicalOemSerialNum, slEntPhysicalProductionDate=slEntPhysicalProductionDate, slEntPhysicalSerialNum=slEntPhysicalSerialNum, slmEntity=slmEntity, slEntPhysicalProtectMode=slEntPhysicalProtectMode, slEntPhysicalPartNumber=slEntPhysicalPartNumber, slEntPhysicalCleiCode=slEntPhysicalCleiCode, slEntPhysicalFirmwareRev=slEntPhysicalFirmwareRev, PYSNMP_MODULE_ID=slmEntity, slEntityPhysical=slEntityPhysical, PhysicalIndex=PhysicalIndex, slEntPhysicalIndex=slEntPhysicalIndex, slEntPhysicalDescr=slEntPhysicalDescr, slEntPhysicalSysTemp=slEntPhysicalSysTemp, slEntPhysicalType=slEntPhysicalType)
