#
# PySNMP MIB module NBS-FEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FEC-MIB
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsFecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 232))
if mibBuilder.loadTexts: nbsFecMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsFecMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsFecMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsFecMib.setDescription('Forward Error Correction')
class NbsFecCode(TextualConvention, Integer32):
    description = 'Particular FEC Algorithm/Code'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("notSupported", 0), ("noFec", 1), ("zero", 2), ("gfec", 3), ("ufec7", 4), ("ufec10", 5), ("ufec25", 6), ("hgfec7", 7), ("sdfec0", 8), ("sdfec1", 9), ("sdfec2", 10), ("sdfec3", 11), ("g975i4", 12), ("g975i7", 13), ("xfec7", 14), ("sdfec15", 15))

nbsFecCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 232, 1))
if mibBuilder.loadTexts: nbsFecCfgGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgGrp.setDescription('FEC configuration')
nbsFecCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 232, 1, 1), )
if mibBuilder.loadTexts: nbsFecCfgTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgTable.setDescription('FEC settings for all supported ports')
nbsFecCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1), ).setIndexNames((0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"))
if mibBuilder.loadTexts: nbsFecCfgEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgEntry.setDescription('FEC settings for an individual port')
nbsFecCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setDescription('The mib2 ifIndex')
nbsFecCfgCodeCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setDescription('This bitmask indicates which FEC codes this port can\n        support.\n\n        Bit 0 is reserved.\n\n        Subsequent bits refer to the NbsFecCode enumerated list.  Bit 1\n        corresponds to none(1), Bit 2 to zero(2) enumeration,\n        and so on.  A bit is set (1) if that code is appropriate\n        for this module, cleared (0) if unavailable.\n\n        OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
nbsFecCfgCodeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3), NbsFecCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setDescription('The administratively desired Forward Error Correction code')
nbsFecCfgCodeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4), NbsFecCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setDescription('The operationally active Forward Error Correction code')
mibBuilder.exportSymbols("NBS-FEC-MIB", nbsFecCfgCodeOper=nbsFecCfgCodeOper, NbsFecCode=NbsFecCode, nbsFecCfgCodeCaps=nbsFecCfgCodeCaps, nbsFecCfgTable=nbsFecCfgTable, nbsFecMib=nbsFecMib, nbsFecCfgCodeAdmin=nbsFecCfgCodeAdmin, nbsFecCfgGrp=nbsFecCfgGrp, nbsFecCfgIfIndex=nbsFecCfgIfIndex, nbsFecCfgEntry=nbsFecCfgEntry, PYSNMP_MODULE_ID=nbsFecMib)
