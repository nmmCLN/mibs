#
# PySNMP MIB module GARDEROS-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 10:06:47 2022
# On host fv-az377-643 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
garderos, = mibBuilder.importSymbols("GARDEROS-SMI-MIB", "garderos")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ObjectIdentity, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, MibIdentifier, Counter64, Counter32, Gauge32, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "IpAddress", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
product = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108, 1))
product.setRevisions(('2017-03-06 13:59',))
if mibBuilder.loadTexts: product.setLastUpdated('201703061359Z')
if mibBuilder.loadTexts: product.setOrganization('Garderos GmbH')
productMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1))
if mibBuilder.loadTexts: productMIB.setStatus('current')
productConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2))
if mibBuilder.loadTexts: productConformance.setStatus('current')
productGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1))
if mibBuilder.loadTexts: productGroups.setStatus('current')
productCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2))
if mibBuilder.loadTexts: productCompliances.setStatus('current')
productModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2, 1)).setObjects(("GARDEROS-PRODUCT-MIB", "productInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productModuleCompliance = productModuleCompliance.setStatus('current')
productInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1, 2)).setObjects(("GARDEROS-PRODUCT-MIB", "productType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productInformationGroup = productInformationGroup.setStatus('current')
productCasingType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17))
if mibBuilder.loadTexts: productCasingType.setStatus('current')
productCasing = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33))
if mibBuilder.loadTexts: productCasing.setStatus('current')
productMainboard = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31))
if mibBuilder.loadTexts: productMainboard.setStatus('current')
productInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36))
if mibBuilder.loadTexts: productInterfaces.setStatus('current')
productSubType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255))
if mibBuilder.loadTexts: productSubType.setStatus('current')
productGeneral = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1))
if mibBuilder.loadTexts: productGeneral.setStatus('current')
productType = MibScalar((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productType.setStatus('current')
mibBuilder.exportSymbols("GARDEROS-PRODUCT-MIB", productInformationGroup=productInformationGroup, productInterfaces=productInterfaces, productGroups=productGroups, productConformance=productConformance, PYSNMP_MODULE_ID=product, productModuleCompliance=productModuleCompliance, productCompliances=productCompliances, productMIB=productMIB, productGeneral=productGeneral, productMainboard=productMainboard, productType=productType, productCasing=productCasing, product=product, productCasingType=productCasingType, productSubType=productSubType)
