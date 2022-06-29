#
# PySNMP MIB module NBS-META-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-META-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:43 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, ObjectIdentity, Integer32, Bits, MibIdentifier, ModuleIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ObjectIdentity", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsMetaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 205))
if mibBuilder.loadTexts: nbsMetaMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsMetaMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsMetaMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsMetaMib.setDescription('MIB for representing NBS FDRNIX private information')
nbsMetaMibGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 205, 1))
if mibBuilder.loadTexts: nbsMetaMibGrp.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibGrp.setDescription('Meta MIB')
nbsMetaMibFeatureTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 205, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureTableSize.setDescription('The number of rows in the nbsMetaMibFeature table')
nbsMetaMibFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 629, 205, 1, 2), )
if mibBuilder.loadTexts: nbsMetaMibFeatureTable.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureTable.setDescription('List of features a hardware device might implement.')
nbsMetaMibFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1), ).setIndexNames((0, "NBS-META-MIB", "nbsMetaMibFeatureID"))
if mibBuilder.loadTexts: nbsMetaMibFeatureEntry.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureEntry.setDescription('A specific feature')
nbsMetaMibFeatureID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: nbsMetaMibFeatureID.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureID.setDescription('Unique identifier for this feature')
nbsMetaMibFeatureFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureFamily.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureFamily.setDescription('Family of this feature')
nbsMetaMibFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureName.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureName.setDescription('Name of this feature')
nbsMetaMibFeatureDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureDesc.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureDesc.setDescription('Description of this feature and its settings')
nbsMetaMibFeatureUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureUnits.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureUnits.setDescription('The units used in this feature')
nbsMetaMibFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enum", 1), ("string", 2), ("integer", 3), ("float", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureType.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibFeatureType.setDescription('Data type')
nbsMetaMibVariableTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 205, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableTableSize.setDescription('The number of rows in the nbsMetaMibVariable table')
nbsMetaMibVariableTable = MibTable((1, 3, 6, 1, 4, 1, 629, 205, 1, 4), )
if mibBuilder.loadTexts: nbsMetaMibVariableTable.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableTable.setDescription('List of variables a specific device implements.')
nbsMetaMibVariableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1), ).setIndexNames((0, "NBS-META-MIB", "nbsMetaMibVariableIfIndex"), (0, "NBS-META-MIB", "nbsMetaMibVariableID"))
if mibBuilder.loadTexts: nbsMetaMibVariableEntry.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableEntry.setDescription('A specific feature')
nbsMetaMibVariableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsMetaMibVariableIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableIfIndex.setDescription('What CCSSPPP does this belong to? If SS and PPP are zero, this\n           belongs to a chassis. If PPP is zero, this belongs to a slot.')
nbsMetaMibVariableID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsMetaMibVariableID.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableID.setDescription('Index into nbsMetaMibFeatureTable (nbsMetaMibFeatureID).')
nbsMetaMibVariableCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableCaps.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableCaps.setDescription('A list of comma separated strings that indicate what values\n           this variable supports. Ranges and string lengths are\n           expressed as a two item list (MIN,MAX). A zero length string\n           indicates this variable is read only.')
nbsMetaMibVariableDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableDefault.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableDefault.setDescription('Default value of this variable. It may report a zero length\n           string if FeatureType is string.')
nbsMetaMibVariableJumper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableJumper.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableJumper.setDescription("Current jumper setting for this variable. If the current\n           jumper setting cannot be reported:\n\n               - VariableJumper will report 'N/A' if FeatureType is\n                 string.\n               - VariableJumper will be zero length otherwise.\n\n           If FeatureType is string, a zero length VariableJumper is\n           a valid value.")
nbsMetaMibVariableOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableOper.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableOper.setDescription("Current operational value for this variable. If the current\n           operational value cannot be reported:\n\n               - VariableOper will report 'N/A' if FeatureType is\n                 string.\n               - VariableOper will be zero length otherwise.\n\n           If VariableOper reports not supported, but VariableCaps\n           reports non-zero length, this variable is write-only.\n\n           If FeatureType is string, a zero length VariableOper is\n           a valid value.")
nbsMetaMibVariableAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsMetaMibVariableAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableAdmin.setDescription('Administrative value of this variable. If the administrative\n           value cannot be set for this variable, VariableCaps will\n           report a zero length string when read.\n\n           Writing zero length values are only permitted if FeatureType\n           is string and VariableCaps permits it. Otherwise, zero\n           length strings will be rejected.\n\n           If FeatureType is string, a zero length VariableAdmin is\n           a valid value.')
nbsMetaMibVariableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableStatus.setStatus('current')
if mibBuilder.loadTexts: nbsMetaMibVariableStatus.setDescription('Messages relating to this variable')
mibBuilder.exportSymbols("NBS-META-MIB", nbsMetaMibVariableID=nbsMetaMibVariableID, nbsMetaMibVariableOper=nbsMetaMibVariableOper, nbsMetaMibVariableJumper=nbsMetaMibVariableJumper, nbsMetaMibFeatureFamily=nbsMetaMibFeatureFamily, nbsMetaMibVariableStatus=nbsMetaMibVariableStatus, nbsMetaMibVariableTableSize=nbsMetaMibVariableTableSize, PYSNMP_MODULE_ID=nbsMetaMib, nbsMetaMibFeatureEntry=nbsMetaMibFeatureEntry, nbsMetaMibFeatureName=nbsMetaMibFeatureName, nbsMetaMibVariableTable=nbsMetaMibVariableTable, nbsMetaMibVariableAdmin=nbsMetaMibVariableAdmin, nbsMetaMibVariableEntry=nbsMetaMibVariableEntry, nbsMetaMibFeatureTable=nbsMetaMibFeatureTable, nbsMetaMib=nbsMetaMib, nbsMetaMibFeatureID=nbsMetaMibFeatureID, nbsMetaMibFeatureDesc=nbsMetaMibFeatureDesc, nbsMetaMibFeatureTableSize=nbsMetaMibFeatureTableSize, nbsMetaMibVariableCaps=nbsMetaMibVariableCaps, nbsMetaMibVariableIfIndex=nbsMetaMibVariableIfIndex, nbsMetaMibGrp=nbsMetaMibGrp, nbsMetaMibFeatureUnits=nbsMetaMibFeatureUnits, nbsMetaMibVariableDefault=nbsMetaMibVariableDefault, nbsMetaMibFeatureType=nbsMetaMibFeatureType)
