#
# PySNMP MIB module SENSATRONICS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-SMI
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:19 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ModuleIdentity, Integer32, MibIdentifier, enterprises, ObjectIdentity, Counter64, TimeTicks, NotificationType, IpAddress, Unsigned32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ModuleIdentity", "Integer32", "MibIdentifier", "enterprises", "ObjectIdentity", "Counter64", "TimeTicks", "NotificationType", "IpAddress", "Unsigned32", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sensatronics = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174))
sensatronics.setRevisions(('2004-04-20 00:00',))
if mibBuilder.loadTexts: sensatronics.setLastUpdated('200404200000Z')
if mibBuilder.loadTexts: sensatronics.setOrganization('Sensatronics LLC')
consumerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1))
if mibBuilder.loadTexts: consumerProducts.setStatus('current')
envMonitors = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1))
if mibBuilder.loadTexts: envMonitors.setStatus('current')
consumerTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 2))
if mibBuilder.loadTexts: consumerTools.setStatus('current')
customProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 3))
if mibBuilder.loadTexts: customProducts.setStatus('current')
customTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 4))
if mibBuilder.loadTexts: customTools.setStatus('current')
productITTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1))
if mibBuilder.loadTexts: productITTM.setStatus('current')
productCRYO = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 2))
if mibBuilder.loadTexts: productCRYO.setStatus('current')
productEM1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3))
if mibBuilder.loadTexts: productEM1.setStatus('current')
mibBuilder.exportSymbols("SENSATRONICS-SMI", customProducts=customProducts, productCRYO=productCRYO, productEM1=productEM1, consumerTools=consumerTools, consumerProducts=consumerProducts, PYSNMP_MODULE_ID=sensatronics, productITTM=productITTM, envMonitors=envMonitors, sensatronics=sensatronics, customTools=customTools)
