#
# PySNMP MIB module CTRON-IF-REMAP-2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-IF-REMAP-2-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:46 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ctIFRemap2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctIFRemap2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctIFRemap2Config = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1))
ctIFRemap2Table = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1), )
if mibBuilder.loadTexts: ctIFRemap2Table.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2Table.setDescription('This table provides the ability to remap all frames from one\n            port onto another port.  A port is defined by \nctIFRemap2PortIndex\n            from the ctIFRemap2PortTable below.  Only ports listed in the\n            ctIFRemap2PortTable are available for remapping.\n\n            A given source port may only be mapped to only one destination \n            port.  Once a port is reserved as part of a ctIFRemap2Table  entry,\n            it may not be used in any other ctIFRemap2Table entries (ie. If \n            remapping port 1 to port 3, then neither port 1 or port 3 may be\n            used as a ctIFRemap2SourcePort or ctIFRemap2DestPort in another\n            ctIFRemap2Table entry).\n\n            Each row that exists in this table defines such a relationship.\n            By disabling a row in this table the remapping relationship no \n            longer exists.\n\n            Each entry will be referenced by slot.  In the case of a\n            stand-alone device the slot will always be 1.\n\n            If a given relationship cannot be created the set will fail\n            with a BAD-VALUE error.')
ctIFRemap2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourceSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourcePort"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestPort"))
if mibBuilder.loadTexts: ctIFRemap2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2Entry.setDescription('Describes a particular ifremap entry.')
ctIFRemap2SourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SourceSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SourceSlot.setDescription('The slot combined with the ctIFRemap2SourcePort which will\n            have all packets redirected to the destination port as defined\n            by ctIFRemap2DestSlot and ctIFRemap2DestPort.')
ctIFRemap2SourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SourcePort.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SourcePort.setDescription('The port combined with the ctIFRemap2SourceSlot which will\n            have all packets redirected to the destination port as defined\n            by ctIFRemap2DestSlot and ctIFRemap2DestPort.')
ctIFRemap2DestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2DestSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2DestSlot.setDescription('The slot combined with the ctIFRemap2DestPort which will\n            see all packets redirected from ctIFRemap2SourceSlot and\n            ctIFRemap2SourcePort.')
ctIFRemap2DestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2DestPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2DestPort.setDescription('The port combined with the ctIFRemap2DestSlot which will\n            see all packets redirected from ctIFRemap2SourceSlot and\n            ctIFRemap2SourcePort.')
ctIFRemap2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2Status.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2Status.setDescription('Defines the status of the ifremap entry.  Setting\n            ctIFRemap2Status to a value of enable(1) has the effect of\n            creating an entry in the table when it does not already exist.\n            Setting ctIFRemap2Status to a value of disable(2) disables the\n            entry and deletes the row from the table.  Therefore this\n            table only contains entries that are active.')
ctIFRemap2PhysicalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unsupported", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2PhysicalErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PhysicalErrors.setDescription('Enable or disable remapping of physical errors.  This object\n            controls whether or not frames with physical errors should be\n            remapped out the destination port for this entry.  By default,\n            this will be enabled when an entry is created.\n            \n            NOTE: This action is always superseded by the value of\n            ctIFRemap2PhysErrsCapable for either the source or destination\n            port specified in this remap entry.  If a port is not\n            physically capable of transmitting or receiving error frames,\n            then this object will return unsupported(3) and the value\n            cannot be changed.')
ctIFRemap2EgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("alwaysTagged", 2), ("alwaysUntagged", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2EgressType.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2EgressType.setDescription('Defines how each packet will be tagged when sent out the \n             ctIFRemap2DestPort.  Setting ctIFRemap2EgressType to normal(1)\n             will set packets to be sent out as they are seen by \n             ctIFRemap2SourcePort.  Setting ctIFRemap2EgressType to \n             alwaysTagged(2) will set packets to always be sent out \n             ctIFRemap2DestSlot and ctIFRemap2DestPort with a tag. Setting \n             ctIFRemap2EgressType to alwaysUntagged(3) will set packets to always \n             be sent out ctIFRemap2DestSlot and ctIFRemap2DestPort without a tag.\n             If the module is not configured to support packet tagging (i.e. 802.1d \n             bridge mode) then setting this object to alwaysTagged(2) or \n             alwaysUntagged(3) will return a BAD-VALUE error.')
ctIFRemap2PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2), )
if mibBuilder.loadTexts: ctIFRemap2PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PortTable.setDescription('This table holds all valid ports that are remappable or\n            able to accept a remapped packet.')
ctIFRemap2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortIndex"))
if mibBuilder.loadTexts: ctIFRemap2PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PortEntry.setDescription('Describes a particular supported remappable port.')
ctIFRemap2PortSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PortSlot.setDescription('Defines the slot in which the remap capable module resides. \n            In the case of a stand-alone device the slot will always be 1.')
ctIFRemap2PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PortIndex.setDescription('Defines an port that is remappable or is able to accept a\n            remapped packet.  Ideally indices will start with 1 and will\n            be numbered continuously through the number of available remap\n            ports.  However, this need not necessarily be the case.\n            Indices may be sparse and begin with any number if desired\n            for a particular implementation.')
ctIFRemap2PortReference = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PortReference.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PortReference.setDescription('This object returns an OID referencing an object which\n             uniquely corresponds to this remap port.  The only criteria\n             is that this OID is a leaf, and that it exists and is\n             accessible.  For example, if remap functionality is running\n             on an 802.1d compliant bridge, remap port #1 could reference\n             dot1dBasePort.1. Alternatively you could reference a mib2\n             interface like ifIndex.1 or a Cabletron Secure Fast port.\n             Mixing these types (some refer to bridge ports, others refer\n             to SFS ports) is not advised, but not prohibited')
ctIFRemap2PhysErrsCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2PhysErrsCapable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2PhysErrsCapable.setDescription('Indicate whether the port is incapable of remapping physical\n            errors.  If the capability is supported, this object will\n            return supported(1).  If the capability is unsupported, this\n            object will return unsupported(2).')
ctIFRemap2SlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3), )
if mibBuilder.loadTexts: ctIFRemap2SlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SlotTable.setDescription('This table contains all information pertaining to the\n            abilities or limitations of a particular remap capable\n            module.')
ctIFRemap2SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SlotIndex"))
if mibBuilder.loadTexts: ctIFRemap2SlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SlotEntry.setDescription('Describes a particular entry in the ctIFRemap2SlotTable.\n            Each entry is indexed by the physical slot in which the\n            module resides.')
ctIFRemap2SlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SlotIndex.setDescription('Defines the slot in which the remap capable module resides. \nIn\n            the case of a stand-alone device the slot will always be 1.')
ctIFRemap2SlotMaxRemaps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemaps.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemaps.setDescription('The maximum number of entries allowed to be sourced from the\n            module in this slot in the ctIFRemap2Table.')
ctIFRemap2SlotMaxRemoteDests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemoteDests.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2SlotMaxRemoteDests.setDescription('The maximum number of remote destination ports per remote\n            module.  For example, a value of 3 means that I can have no\n            more than 3 remap destination ports between this module, and\n            any other given module in the same chassis simultaneously. I\n            can have multiple source ports remapped to each of the three\n            remote destination ports.  I can also remap to up to three\n            remote destination ports on each of the other modules in the\n            chassis simultaneously.')
ctIFRemap2VlanTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4), )
if mibBuilder.loadTexts: ctIFRemap2VlanTable.setReference('ctvlan-ext-mib .4.4.1.1')
if mibBuilder.loadTexts: ctIFRemap2VlanTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanTable.setDescription('This table provides the ability to remap all frames from any\n            port on a particular vlan to a specific destination port.  \n            Each row that exists in this table defines such a relationship.\n            By disabling a row in this table the remapping relationship no\n            longer exists.\n\n            Multiple vlans may be mapped to a given destination port \n            (ie. vlan 11 and vlan 35 may both remap to port 10).\n\n            A port is defined by ctIFRemap2PortIndex in the ctIFRemap2PortTable,\n            above.  Only ports listed in the ctIFRemap2PortTable are available\n            for remapping.  A  vlan is defined by ctVlanVID in the\n            ctVlanConfigTable. Only vlans listed in the ctVlanConfigTable are\n            available for remapping.\n\n            Each entry will be referenced by slot.  In the case of a\n            stand-alone device the slot will always be 1.\n\n            If a given relationship cannot be created the set will fail\n            with a BAD-VALUE error.')
ctIFRemap2VlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1), ).setIndexNames((0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceVlan"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestSlot"), (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestPort"))
if mibBuilder.loadTexts: ctIFRemap2VlanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanEntry.setDescription('Describes a particular ifremap Vlan entry.')
ctIFRemap2VlanSourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanSourceSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanSourceSlot.setDescription('The slot combined with the ctIFRemap2VlanSourceVlan which will\n            have all packets redirected to the destination port as defined\n            by ctIFRemap2VlanDestSlot and ctIFRemap2VlanDestPort.')
ctIFRemap2VlanSourceVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanSourceVlan.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanSourceVlan.setDescription('The vlan combined with the ctIFRemap2VlanSourceSlot which will\n            have all packets redirected to the destination port as defined\n            by ctIFRemap2VlanDestSlot and ctIFRemap2VlanDestPort.')
ctIFRemap2VlanDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanDestSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanDestSlot.setDescription('The slot combined with the ctIFRemap2VlanDestPort which will\n            see all packets redirected from ctIFRemap2VlanSourceSlot and\n            ctIFRemap2VlanSourceVlan.')
ctIFRemap2VlanDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIFRemap2VlanDestPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanDestPort.setDescription('The port combined with the ctIFRemap2VlanDestSlot which will\n            see all packets redirected from ctIFRemap2VlanSourceSlot and\n            ctIFRemap2VlanSourceVlan.')
ctIFRemap2VlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2VlanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanStatus.setDescription('Defines the status of the ifremap vlan entry.  Setting\n            ctIFRemap2VlanStatus to a value of enable(1) has the effect of\n            creating an entry in the table when it does not already exist.\n            Setting ctIFRemap2VlanStatus to a value of disable(2) disables the\n            entry and deletes the row from the table.  Therefore this\n            table only contains entries that are active.\n   \n            If ctIFRemap2VlanSourceVlan is already being used by another\n            ctIfRemap2Vlan entry or ctifRemap2 Entry then a set to \n            ctIFRemap2VlanStatus of value enable(1) will return with a\n            BAD-VALUE error.')
ctIFRemap2VlanEgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("received", 1), ("alwaysTagged", 2), ("alwaysUntagged", 3))).clone('received')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIFRemap2VlanEgressType.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemap2VlanEgressType.setDescription("Defines how each packet will be tagged when sent out the \n             ctIFRemap2VlanDestPort.  Setting ctIFRemap2VlanEgressType to \n             received(1) will set packets to be sent out ctIFRemap2VlanDestSlot\n             and ctIFRemap2VlanDestPort exactly as they are received by \n             ctIFRemap2VlanSourceVlan. Setting ctIFRemap2VlanEgressType to \n             alwaysTagged(2) will set packets to be sent out \n             ctIFRemap2VlanDestSlot and ctIFRemap2VlanDestPort with the \n             vlan tag associated with ctIFRemap2VlanSourceVlan.  If this port\n             does not have a vlan tag associated with it then all packets will\n             be remapped without a tag.  Setting ctIFRemap2VlanEgressType to\n             alwaysUntagged(3) will set packets to be sent out \n             ctIFRemap2VlanDestSlot and ctIFRemap2VlanDestPort without any\n             tag reguardless of ctIFRemap2VlanSourceVlan's tagging status.")
mibBuilder.exportSymbols("CTRON-IF-REMAP-2-MIB", ctIFRemap2VlanEgressType=ctIFRemap2VlanEgressType, ctIFRemap2VlanSourceSlot=ctIFRemap2VlanSourceSlot, ctIFRemap2Entry=ctIFRemap2Entry, ctIFRemap2VlanSourceVlan=ctIFRemap2VlanSourceVlan, ctIFRemap2PortEntry=ctIFRemap2PortEntry, ctIFRemap2DestPort=ctIFRemap2DestPort, ctIFRemap2VlanStatus=ctIFRemap2VlanStatus, ctIFRemap2PortTable=ctIFRemap2PortTable, ctIFRemap2Table=ctIFRemap2Table, ctIFRemap2Status=ctIFRemap2Status, ctIFRemap2PhysicalErrors=ctIFRemap2PhysicalErrors, ctIFRemap2VlanDestSlot=ctIFRemap2VlanDestSlot, ctIFRemap2SlotIndex=ctIFRemap2SlotIndex, ctIFRemap2VlanEntry=ctIFRemap2VlanEntry, ctIFRemap2SourceSlot=ctIFRemap2SourceSlot, ctIFRemap2PortIndex=ctIFRemap2PortIndex, ctIFRemap2DestSlot=ctIFRemap2DestSlot, ctIFRemap2PortSlot=ctIFRemap2PortSlot, ctIFRemap2SlotMaxRemaps=ctIFRemap2SlotMaxRemaps, ctIFRemap2SlotTable=ctIFRemap2SlotTable, ctIFRemap2Config=ctIFRemap2Config, ctIFRemap2SlotEntry=ctIFRemap2SlotEntry, ctIFRemap2PhysErrsCapable=ctIFRemap2PhysErrsCapable, ctIFRemap2SourcePort=ctIFRemap2SourcePort, ctIFRemap2SlotMaxRemoteDests=ctIFRemap2SlotMaxRemoteDests, ctIFRemap2PortReference=ctIFRemap2PortReference, ctIFRemap2VlanTable=ctIFRemap2VlanTable, ctIFRemap2EgressType=ctIFRemap2EgressType, ctIFRemap2VlanDestPort=ctIFRemap2VlanDestPort)
