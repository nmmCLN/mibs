#
# PySNMP MIB module HIPATH-WIRELESS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ewc/HIPATH-WIRELESS-SMI
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, NotificationType, Counter64, Integer32, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "Counter64", "Integer32", "ObjectIdentity", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hiPathWireless = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 15))
hiPathWireless.setRevisions(('2005-07-21 02:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hiPathWireless.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hiPathWireless.setLastUpdated('200507210237Z')
if mibBuilder.loadTexts: hiPathWireless.setOrganization('Chantry Networks, Inc.')
if mibBuilder.loadTexts: hiPathWireless.setContactInfo('Behrouz Sultan\n\t\t\t\tChantry Networks, Inc.\n\t\t\t\t\n\t\t\t\t1900 Minnesota Court, Suite 125\n\t\t\t\tMississauga ON, L5N 3C9\n\t\t\t\t\n\t\t\t\tEmail: behrouz.sultan@siemens.com\n\t\t\t\tPhone 1-905-363-6400\n\t\t\t\tFax   1-905-567-0099')
if mibBuilder.loadTexts: hiPathWireless.setDescription('The root MIB module for High Path Wireless Products.\n\t\t\t\tenterprises.siemens(4329).15')
siemens = MibIdentifier((1, 3, 6, 1, 4, 1, 4329))
hiPathWirelessProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1))
if mibBuilder.loadTexts: hiPathWirelessProducts.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessProducts.setDescription('Provides a root OID from which MIB-II sysObjectID values \n\t\t\t\tare assigned. Actual product OIDs are defined in\n\t\t\t\tHIPATH-WIRELESS-PRODUCTS-MIB.')
hiPathWirelessMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 3))
if mibBuilder.loadTexts: hiPathWirelessMgmt.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessMgmt.setDescription('Main subtree for High Path Wireless Networks management information.')
hiPathWirelessDevelopment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 4))
if mibBuilder.loadTexts: hiPathWirelessDevelopment.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessDevelopment.setDescription("Subtree for pre-release MIB development. \n\t\t\t\tElements in this subtree are eventually moved to \n\t\t\t\t'hiPathWirelessMgmt'.")
hiPathWirelessModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 5))
if mibBuilder.loadTexts: hiPathWirelessModules.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessModules.setDescription('Provides a root object identifier from which\n\t\t\t\tMODULE-IDENTITY values are assigned.')
hiPathWirelessHWM = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 6))
if mibBuilder.loadTexts: hiPathWirelessHWM.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessHWM.setDescription('Sub-tree for Hipath Wireless Manager Application and its associated applications.')
mibBuilder.exportSymbols("HIPATH-WIRELESS-SMI", hiPathWirelessModules=hiPathWirelessModules, siemens=siemens, PYSNMP_MODULE_ID=hiPathWireless, hiPathWirelessProducts=hiPathWirelessProducts, hiPathWireless=hiPathWireless, hiPathWirelessHWM=hiPathWirelessHWM, hiPathWirelessDevelopment=hiPathWirelessDevelopment, hiPathWirelessMgmt=hiPathWirelessMgmt)
