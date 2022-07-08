#
# PySNMP MIB module NBS-OTNOH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OTNOH-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:24:43 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Unsigned32, Bits, ModuleIdentity, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "iso", "Counter64", "NotificationType")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
nbsOtnohMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 224))
if mibBuilder.loadTexts: nbsOtnohMib.setLastUpdated('201212200000Z')
if mibBuilder.loadTexts: nbsOtnohMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsOtnohMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsOtnohMib.setDescription('OTN/SONET Overhead fields')
nbsOtnohTtiGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 224, 1))
if mibBuilder.loadTexts: nbsOtnohTtiGrp.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiGrp.setDescription('OTN overhead fields')
nbsOtnohTtiTable = MibTable((1, 3, 6, 1, 4, 1, 629, 224, 1, 1), )
if mibBuilder.loadTexts: nbsOtnohTtiTable.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiTable.setDescription('OTN Trail Trace Identifier values')
nbsOtnohTtiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1), ).setIndexNames((0, "NBS-OTNOH-MIB", "nbsOtnohTtiIfIndex"), (0, "NBS-OTNOH-MIB", "nbsOtnohTtiScope"))
if mibBuilder.loadTexts: nbsOtnohTtiEntry.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiEntry.setDescription('Trail Trace Identifier (TTI) values for a particular interface.\n\n         Per ITU-T G.709, a TTI has 64 bytes; the first 16 contain the\n         Source Access Point Identifer (SAPI), the next 16 contain the\n         Destination Access Point Identifer (SAPI), and the final 32\n         contain an Operator Specific value.\n\n         For the SAPI and DAPI, the first byte is all zero, and the other\n         fifteen are seven-bit International Reference Alphabet (IRA)\n         characters; ACSII is the USA variant. There is a three character\n         international segment field followed by a twelve character\n         national segment field, which consists of two subfields: the\n         ITU carrier code (ICC) and a unique access point code (UAPC).')
nbsOtnohTtiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsOtnohTtiIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiIfIndex.setDescription('The mib2 ifIndex')
nbsOtnohTtiScope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("tcm1", 1), ("tcm2", 2), ("tcm3", 3), ("tcm4", 4), ("tcm5", 5), ("tcm6", 6), ("section", 7), ("path", 8))))
if mibBuilder.loadTexts: nbsOtnohTtiScope.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiScope.setDescription('This object specifies the TTI field that the following row values\n        apply.')
nbsOtnohTtiSendSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendSapi.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiSendSapi.setDescription('This object specifies the Source Access Point Identifier (SAPI)\n        byte value(s) to send in the selected TTI field of outgoing OTN\n        frames. There are sixteen bytes in the SAPI. Any bytes unspecified\n        by this string will be set to zero.')
nbsOtnohTtiSendDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendDapi.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiSendDapi.setDescription('This object specifies the Destination Access Point Identifier (DAPI)\n        byte value(s) to send in the selected TTI field of outgoing OTN\n        frames. There are sixteen bytes in the DAPI. Any bytes unspecified\n        by this string will be set to zero.')
nbsOtnohTtiSendOpSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiSendOpSpec.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiSendOpSpec.setDescription('This object specifies the Operator Specfic\n        byte value(s) to send in the selected TTI field of outgoing OTN\n        frames. There are thirty-two bytes in the SAPI. Any bytes unspecified\n        by this string will be set to zero.')
nbsOtnohTtiExpectSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectSapi.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiExpectSapi.setDescription('This object specifies the sixteen byte Source Access Point\n        Identifier (SAPI) value to expect in the selected TTI field of\n        incoming OTN frames. A zero length octet string indicates no SAPI\n        matching is desired.')
nbsOtnohTtiExpectDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectDapi.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiExpectDapi.setDescription('This object specifies the sixteen byte Destination Access Point\n        Identifier (DAPI) value to expect in the selected TTI field of\n        incoming OTN frames. A zero length octet string indicates no DAPI\n        matching is desired.')
nbsOtnohTtiExpectOpSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiExpectOpSpec.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiExpectOpSpec.setDescription('This object specifies the thirty-two byte Operator Specfic value\n        to expect in the selected TTI field of incoming OTN frames.\n        A zero length octet string indicates no Operator Specfic\n        matching is desired.')
nbsOtnohTtiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 224, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsOtnohTtiRowStatus.setStatus('current')
if mibBuilder.loadTexts: nbsOtnohTtiRowStatus.setDescription('Used to add/remove the configuration of a network segment')
mibBuilder.exportSymbols("NBS-OTNOH-MIB", nbsOtnohTtiExpectOpSpec=nbsOtnohTtiExpectOpSpec, nbsOtnohTtiGrp=nbsOtnohTtiGrp, nbsOtnohTtiIfIndex=nbsOtnohTtiIfIndex, nbsOtnohTtiSendOpSpec=nbsOtnohTtiSendOpSpec, PYSNMP_MODULE_ID=nbsOtnohMib, nbsOtnohTtiSendDapi=nbsOtnohTtiSendDapi, nbsOtnohTtiScope=nbsOtnohTtiScope, nbsOtnohTtiExpectDapi=nbsOtnohTtiExpectDapi, nbsOtnohTtiSendSapi=nbsOtnohTtiSendSapi, nbsOtnohTtiRowStatus=nbsOtnohTtiRowStatus, nbsOtnohMib=nbsOtnohMib, nbsOtnohTtiEntry=nbsOtnohTtiEntry, nbsOtnohTtiExpectSapi=nbsOtnohTtiExpectSapi, nbsOtnohTtiTable=nbsOtnohTtiTable)
