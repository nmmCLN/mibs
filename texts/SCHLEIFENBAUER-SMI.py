#
# PySNMP MIB module SCHLEIFENBAUER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-SMI
# Produced by pysmi-1.1.8 at Thu Sep 15 09:48:20 2022
# On host fv-az196-500 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Unsigned32, NotificationType, IpAddress, MibIdentifier, ObjectIdentity, TimeTicks, Counter32, iso, ModuleIdentity, enterprises, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter32", "iso", "ModuleIdentity", "enterprises", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
schleifenbauer = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034))
schleifenbauer.setRevisions(('2015-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schleifenbauer.setRevisionsDescriptions(('The initial revision of this MIB module',))
if mibBuilder.loadTexts: schleifenbauer.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauer.setOrganization('Schleifenbauer Engineering')
if mibBuilder.loadTexts: schleifenbauer.setContactInfo('Schleifenbauer Engineering\n         Alain Schuermans\n         Chief Technology Officer\n         Rietwaard 15\n         5236 WC ‘s-Hertogenbosch\n         The Netherlands\n         t +31 (0)73 52 30256\n         f +31 (0)73 521 23 83\n         alain@schleifenbauer.eu\n         www.schleifenbauer.eu')
if mibBuilder.loadTexts: schleifenbauer.setDescription('The Structure of Management Information for the Schleifenbauer\n         enterprise.\n        \n         Copyright (c) 2015 by Schleifenbauer Products BV')
schleifenbauerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 11))
if mibBuilder.loadTexts: schleifenbauerProducts.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerProducts.setDescription('schleifenbauerProducts is the root OBJECT IDENTIFIER from which\n         sysObjectId values are assigned. Acutal values are defined in \n         SCHLEIFENBAUER-PRODUCTS-MIB.')
schleifenbauerMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 12))
if mibBuilder.loadTexts: schleifenbauerMgmt.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerMgmt.setDescription('schleifenbauerMgmt is the main subtree for new mib development.')
schleifenbauerModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 13))
if mibBuilder.loadTexts: schleifenbauerModules.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerModules.setDescription('schleifenbauerModules provides a root object identifier from which\n         MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("SCHLEIFENBAUER-SMI", PYSNMP_MODULE_ID=schleifenbauer, schleifenbauerModules=schleifenbauerModules, schleifenbauerProducts=schleifenbauerProducts, schleifenbauerMgmt=schleifenbauerMgmt, schleifenbauer=schleifenbauer)
