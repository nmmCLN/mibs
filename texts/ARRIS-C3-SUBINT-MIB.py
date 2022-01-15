#
# PySNMP MIB module ARRIS-C3-SUBINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-SUBINT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:59 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, Integer32, Unsigned32, IpAddress, ModuleIdentity, ObjectIdentity, TimeTicks, enterprises, Counter64, Gauge32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "enterprises", "Counter64", "Gauge32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
cmtsC3SubIntMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11))
if mibBuilder.loadTexts: cmtsC3SubIntMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3SubIntMIB.setOrganization('Arris International')
if mibBuilder.loadTexts: cmtsC3SubIntMIB.setContactInfo('   Network Management\n                Postal: Arris International.\n                        4400 Cork Airport Business Park\n                        Cork Airport, Kinsale Road\n                        Cork, Ireland.\n                Tel:    +353 21 7305 800\n                Fax:    +353 21 4321 972')
if mibBuilder.loadTexts: cmtsC3SubIntMIB.setDescription('This MIB manages the Sub-Interface software on the Arris CMTS C3')
dcxSubIntObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1))
dcxSubIntControlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1))
dcxSubIntTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1), )
if mibBuilder.loadTexts: dcxSubIntTable.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntTable.setDescription('Arris C3 Proprietary Sub-Interface table')
dcxSubIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"))
if mibBuilder.loadTexts: dcxSubIntEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntEntry.setDescription('A row in the dcxSubIntTable. An entry in this table exists \n\t\t for each Sub-Interface configured on the CMTS')
dcxSubIntSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094)))
if mibBuilder.loadTexts: dcxSubIntSlotIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntSlotIndex.setDescription('the slot index of the card in the Cmts')
dcxSubIntPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094)))
if mibBuilder.loadTexts: dcxSubIntPortIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntPortIndex.setDescription('the port index of the port on a card')
dcxSubIntSubIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094)))
if mibBuilder.loadTexts: dcxSubIntSubIntIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntSubIntIndex.setDescription('the sub-interface index of the sub-inteface on a port')
dcxSubIntBridgeGroupNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBridgeGroupNum.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBridgeGroupNum.setDescription('bridge-group number which the sub-interface is configured on,\n\t     0 is reserved, 255 indicates not configured in a  bridge-group')
dcxSubIntManagementAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntManagementAccess.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntManagementAccess.setDescription('is management of Cmts allowed through sub-interface ')
dcxSubIntPrimaryIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntPrimaryIpAddress.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntPrimaryIpAddress.setDescription('primary ip address of sub-interface')
dcxSubIntPrimaryIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntPrimaryIpMask.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntPrimaryIpMask.setDescription('primary ip subnet mask of sub-interface')
dcxSubIntPrimaryIpBCastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntPrimaryIpBCastAddress.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntPrimaryIpBCastAddress.setDescription('primary ip subnet broadcast address of sub-interface')
dcxSubIntRelayEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntRelayEnabled.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntRelayEnabled.setDescription('are DHCP packets relayed on this sub-interface ')
dcxSubIntRelayInformationOption = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntRelayInformationOption.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntRelayInformationOption.setDescription('is the information options added to the DHCP packets relayed on this \n\t     sub-interface. Has no effect if dcxSubIntRelayEnabled is False on the \n\t     sub-interface.')
dcxSubIntGiaddrPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("primary", 1), ("policy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntGiaddrPolicy.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntGiaddrPolicy.setDescription('which giaddr is used for DHCP packets relayed from CPEs on this sub-interface,\n\t     off(0) is returned when dcxSubIntRelayEnabled is False,\n\t     primary(1) indicates that the primary address on sub-interface is used, \n\t     policy(2) indicates that the first secondary is used.')
dcxSubIntInboundAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntInboundAclIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntInboundAclIndex.setDescription('which Access Control List is this sub-interface bound to for inbound packets, a value\n\t     of zero indicates no ACL binding for inbound packets on the sub-interface')
dcxSubIntOutgoingAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntOutgoingAclIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntOutgoingAclIndex.setDescription('which Access Control List is this sub-interface bound to for outgoing packets, a value\n\t     of zero indicates no ACL binding for inbound packets on the sub-interface')
dcxSubIntUnboundTag = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntUnboundTag.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntUnboundTag.setDescription('sub-interface encapsulate Vlan Tag value, 0 indicates no tag')
dcxSubIntUnboundTagIsNative = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntUnboundTagIsNative.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntUnboundTagIsNative.setDescription('sub-interface will not generate packets with tags when native\n\t     is configured')
dcxSubIntOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSubIntOperational.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntOperational.setDescription('states if the subinterface is operational or not, factors are dcxSubIntStatus and the\n\t     physical ports oper and admin status')
dcxSubIntStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxSubIntStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntStatus.setDescription('Controls and reflects the status of rows in this table.  \n\t     Rows in this table may be created by either the create-and-go or \n\t     create-and-wait paradigms. There is no restriction on changing \n\t     values in a row of this table while the row is active.')
dcxSubIntIpTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2), )
if mibBuilder.loadTexts: dcxSubIntIpTable.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpTable.setDescription('Arris C3 Proprietary Sub-Interface table')
dcxSubIntIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1), ).setIndexNames((0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntIpIndex"))
if mibBuilder.loadTexts: dcxSubIntIpEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpEntry.setDescription('A row in the dcxSubIntIpTable. An entry in this table exists for \n\t\t each IP address configured on the Sub-Interface identified by \n\t\t the dcxSubIntNumber')
dcxSubIntIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: dcxSubIntIpIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpIndex.setDescription('sub-interface secondary IP address index')
dcxSubIntIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntIpAddress.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpAddress.setDescription('a secondary ip address of sub-interface')
dcxSubIntIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntIpMask.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpMask.setDescription('a secondary ip subnet mask of sub-interface')
dcxSubIntIpBCastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntIpBCastAddress.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpBCastAddress.setDescription('a secondary ip subnet broadcast address \n\t     of sub-interface')
dcxSubIntIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntIpAddressType.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpAddressType.setDescription('primary(1): address is the primary address on\n\t        the sub-interface, only one allowed\n\t     secondary(2):address is one of the secondary\n\t        addresses configured on the sub-interface')
dcxSubIntIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxSubIntIpStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntIpStatus.setDescription('Controls and reflects the status of rows in this table.  \n\t     Rows in this table may be created by the create-and-go \n\t     paradigm. There is no restriction on changing values \n\t     in a row of this table while the row is active.')
dcxSubIntCableHelperTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3), )
if mibBuilder.loadTexts: dcxSubIntCableHelperTable.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperTable.setDescription('Arris C3 Proprietary Sub-Interface Cable Helper Table')
dcxSubIntCableHelperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1), ).setIndexNames((0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntCableHelperType"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntCableHelperIndex"))
if mibBuilder.loadTexts: dcxSubIntCableHelperEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperEntry.setDescription('A row in the dcxSubIntCableHelperTable.\n                 An entry in this table exists for each cable helper\n\t\t IP address configured on the Sub-Interface which is \n\t\t identified using the dcxSubIntNumber')
dcxSubIntCableHelperType = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("default", 0), ("cm", 1), ("cpe", 2))))
if mibBuilder.loadTexts: dcxSubIntCableHelperType.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperType.setDescription('category of cable helper address.\n\t     cm(1) these helper addresses are only used when relaying\n\t     DHCP packets originating from a CM.\n\t     cpe(2) these helper addresses are only used when relaying\n\t     DHCP packets originating from a CPE.\n\t     default(0) these helper addresses are used when: \n\t\t- relaying DHCP packets originating from a CM when no \n\t\t  helper address of type cm(1) is configured\n\t\t\t\tor\n\t\t- relaying DHCP packets originating from a CPE when no \n\t\t  helper address of type cpe(2) is configured')
dcxSubIntCableHelperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: dcxSubIntCableHelperIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperIndex.setDescription('sub-interface cable helper index')
dcxSubIntCableHelperIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntCableHelperIpAddress.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperIpAddress.setDescription('cable helper ip address configured on sub-interface')
dcxSubIntCableHelperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxSubIntCableHelperStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntCableHelperStatus.setDescription('Controls and reflects the status of rows in this table.  \n\t     Rows in this table may be created by the create-and-go \n\t     paradigm. Entries in this table can only be created or\n\t     deleted, no modification is possible.')
dcxSubIntVlanTagTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4), )
if mibBuilder.loadTexts: dcxSubIntVlanTagTable.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanTagTable.setDescription('Arris C3 Proprietary Sub-Interface Vlan Tag Table')
dcxSubIntVlanTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1), ).setIndexNames((0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSlotIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntPortIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntSubIntIndex"), (0, "ARRIS-C3-SUBINT-MIB", "dcxSubIntVlanTag"))
if mibBuilder.loadTexts: dcxSubIntVlanTagEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanTagEntry.setDescription('A row in the dcxSubIntVlanTagTable.\n                 An entry in this table exists for each Vlan tag\n\t\t that is configured on the sub-interface (which is \n\t\t identified using the dcxSubIntNumber)')
dcxSubIntVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094)))
if mibBuilder.loadTexts: dcxSubIntVlanTag.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanTag.setDescription('sub-interface Vlan Tag value, 0 indicates no tag')
dcxSubIntVlanNative = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntVlanNative.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanNative.setDescription('sub-interface will not generate packets with tags when native\n\t     is configured')
dcxSubIntVlanIsBound = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntVlanIsBound.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanIsBound.setDescription("is sub-interface tag bound to another sub-interface's VLAN tag")
dcxSubIntBoundVlanSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBoundVlanSlotIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBoundVlanSlotIndex.setDescription('slot index of VLAN tag that dcxSubIntVlanTag is bound to\n\t     -1 when VLAN not bound to another VLAN tag on another\n\t     sub-interface')
dcxSubIntBoundVlanPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBoundVlanPortIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBoundVlanPortIndex.setDescription('port index of VLAN tag that dcxSubIntVlanTag is bound to\n\t     -1 returned when VLAN not bound to another VLAN tag on another\n\t     sub-interface')
dcxSubIntBoundVlanSubIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBoundVlanSubIntIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBoundVlanSubIntIndex.setDescription('sub interface index of VLAN tag that dcxSubIntVlanTag is bound to\n\t     -1 returned when VLAN not bound to another VLAN tag on another\n\t     sub-interface')
dcxSubIntBoundVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBoundVlanTag.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBoundVlanTag.setDescription('sub-interface Vlan Tag value, 0 indicates no tag')
dcxSubIntBoundVlanNative = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSubIntBoundVlanNative.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntBoundVlanNative.setDescription('bound sub-interface will not generate packets with tags when native\n\t     is configured\n\t     FLASE will be returned when VLAN not bound to another VLAN tag on another\n\t     sub-interface')
dcxSubIntVlanTagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 11, 1, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxSubIntVlanTagStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSubIntVlanTagStatus.setDescription('Controls and reflects the status of rows in this table.  \n\t     Rows in this table may be created by the create-and-go \n\t     paradigm. There is no restriction on changing values \n\t     in a row of this table while the row is active.')
mibBuilder.exportSymbols("ARRIS-C3-SUBINT-MIB", dcxSubIntEntry=dcxSubIntEntry, dcxSubIntRelayInformationOption=dcxSubIntRelayInformationOption, dcxSubIntStatus=dcxSubIntStatus, dcxSubIntOutgoingAclIndex=dcxSubIntOutgoingAclIndex, dcxSubIntVlanTagTable=dcxSubIntVlanTagTable, dcxSubIntVlanTagEntry=dcxSubIntVlanTagEntry, dcxSubIntOperational=dcxSubIntOperational, PYSNMP_MODULE_ID=cmtsC3SubIntMIB, dcxSubIntIpTable=dcxSubIntIpTable, dcxSubIntManagementAccess=dcxSubIntManagementAccess, dcxSubIntTable=dcxSubIntTable, dcxSubIntVlanTagStatus=dcxSubIntVlanTagStatus, dcxSubIntPrimaryIpMask=dcxSubIntPrimaryIpMask, dcxSubIntIpBCastAddress=dcxSubIntIpBCastAddress, dcxSubIntCableHelperStatus=dcxSubIntCableHelperStatus, dcxSubIntCableHelperIndex=dcxSubIntCableHelperIndex, dcxSubIntVlanNative=dcxSubIntVlanNative, dcxSubIntIpStatus=dcxSubIntIpStatus, dcxSubIntPrimaryIpAddress=dcxSubIntPrimaryIpAddress, dcxSubIntCableHelperIpAddress=dcxSubIntCableHelperIpAddress, dcxSubIntBoundVlanSubIntIndex=dcxSubIntBoundVlanSubIntIndex, dcxSubIntUnboundTagIsNative=dcxSubIntUnboundTagIsNative, dcxSubIntObjects=dcxSubIntObjects, dcxSubIntPrimaryIpBCastAddress=dcxSubIntPrimaryIpBCastAddress, dcxSubIntVlanIsBound=dcxSubIntVlanIsBound, cmtsC3SubIntMIB=cmtsC3SubIntMIB, dcxSubIntIpAddress=dcxSubIntIpAddress, dcxSubIntSlotIndex=dcxSubIntSlotIndex, dcxSubIntIpMask=dcxSubIntIpMask, dcxSubIntBridgeGroupNum=dcxSubIntBridgeGroupNum, dcxSubIntSubIntIndex=dcxSubIntSubIntIndex, dcxSubIntCableHelperEntry=dcxSubIntCableHelperEntry, dcxSubIntRelayEnabled=dcxSubIntRelayEnabled, dcxSubIntUnboundTag=dcxSubIntUnboundTag, dcxSubIntIpAddressType=dcxSubIntIpAddressType, dcxSubIntBoundVlanPortIndex=dcxSubIntBoundVlanPortIndex, dcxSubIntInboundAclIndex=dcxSubIntInboundAclIndex, dcxSubIntVlanTag=dcxSubIntVlanTag, dcxSubIntIpIndex=dcxSubIntIpIndex, dcxSubIntGiaddrPolicy=dcxSubIntGiaddrPolicy, dcxSubIntControlGroup=dcxSubIntControlGroup, dcxSubIntCableHelperType=dcxSubIntCableHelperType, dcxSubIntBoundVlanSlotIndex=dcxSubIntBoundVlanSlotIndex, dcxSubIntIpEntry=dcxSubIntIpEntry, dcxSubIntBoundVlanTag=dcxSubIntBoundVlanTag, dcxSubIntPortIndex=dcxSubIntPortIndex, dcxSubIntCableHelperTable=dcxSubIntCableHelperTable, dcxSubIntBoundVlanNative=dcxSubIntBoundVlanNative)
