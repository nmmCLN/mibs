#
# PySNMP MIB module GREENBONE-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/greenbone/GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 13:59:02 2023
# On host fv-az565-495 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, TimeTicks, Bits, NotificationType, Counter32, Counter64, Unsigned32, enterprises, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "Bits", "NotificationType", "Counter32", "Counter64", "Unsigned32", "enterprises", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
greenboneProduct = ModuleIdentity((1, 3, 6, 1, 4, 1, 35847, 1))
greenboneProduct.setRevisions(('2017-05-15 00:01', '2015-01-06 00:01', '2014-12-31 00:01', '2012-03-26 00:01',))
if mibBuilder.loadTexts: greenboneProduct.setLastUpdated('201705150001Z')
if mibBuilder.loadTexts: greenboneProduct.setOrganization('Greenbone Networks GmbH')
productName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
productHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 2))
productSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 3))
productGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 4))
hwName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwName.setStatus('current')
swName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swName.setStatus('current')
swVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2))
swVersionString = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionString.setStatus('current')
swVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionMajor.setStatus('current')
swVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionMinor.setStatus('current')
swVersionPatch = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionPatch.setStatus('current')
swVersionRevision = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionRevision.setStatus('current')
greenboneProductGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 1)).setObjects(("GREENBONE-PRODUCT-MIB", "productName"), ("GREENBONE-PRODUCT-MIB", "hwName"), ("GREENBONE-PRODUCT-MIB", "swName"), ("GREENBONE-PRODUCT-MIB", "swVersionString"), ("GREENBONE-PRODUCT-MIB", "swVersionMajor"), ("GREENBONE-PRODUCT-MIB", "swVersionMinor"), ("GREENBONE-PRODUCT-MIB", "swVersionPatch"), ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductGroup = greenboneProductGroup.setStatus('current')
greenboneProductHWGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 2)).setObjects(("GREENBONE-PRODUCT-MIB", "hwName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductHWGroup = greenboneProductHWGroup.setStatus('current')
greenboneProductSWGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 3)).setObjects(("GREENBONE-PRODUCT-MIB", "swName"), ("GREENBONE-PRODUCT-MIB", "swVersionString"), ("GREENBONE-PRODUCT-MIB", "swVersionMajor"), ("GREENBONE-PRODUCT-MIB", "swVersionMinor"), ("GREENBONE-PRODUCT-MIB", "swVersionPatch"), ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductSWGroup = greenboneProductSWGroup.setStatus('current')
mibBuilder.exportSymbols("GREENBONE-PRODUCT-MIB", swVersionString=swVersionString, swVersionMajor=swVersionMajor, greenboneProductGroup=greenboneProductGroup, greenboneProductHWGroup=greenboneProductHWGroup, swVersion=swVersion, hwName=hwName, greenboneProduct=greenboneProduct, productGroups=productGroups, productName=productName, swVersionMinor=swVersionMinor, productSoftware=productSoftware, greenboneProductSWGroup=greenboneProductSWGroup, swVersionRevision=swVersionRevision, productHardware=productHardware, PYSNMP_MODULE_ID=greenboneProduct, swName=swName, swVersionPatch=swVersionPatch)
