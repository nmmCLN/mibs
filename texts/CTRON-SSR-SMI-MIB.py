#
# PySNMP MIB module CTRON-SSR-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SMI-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 15:52:29 2022
# On host fv-az267-189 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, NotificationType, Integer32, iso, Counter32, Counter64, Gauge32, Unsigned32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "Integer32", "iso", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ssr = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501))
ssr.setRevisions(('2000-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ssr.setRevisionsDescriptions(('Update contact information for Riverstone Networks as this mib\n          is found on the Riverstione RS product line and Enterasys SSR product line.',))
if mibBuilder.loadTexts: ssr.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssr.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ssr.setContactInfo('Enterasys Networks\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@enterasys.com\n     http://www.enterasys.com')
if mibBuilder.loadTexts: ssr.setDescription('This mib module defines enterprise MIBs under Cabletron\n         enterprise OID that manage Enterasys SmartSwitch Routers \n         and Riverstone Networks RS product Line.')
ssrMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1))
if mibBuilder.loadTexts: ssrMibs.setStatus('current')
if mibBuilder.loadTexts: ssrMibs.setDescription('All Smart Switch Router (SSR) enterprise MIBs are defined under mibs')
ssrTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 10))
if mibBuilder.loadTexts: ssrTraps.setStatus('current')
if mibBuilder.loadTexts: ssrTraps.setDescription('All enterprise traps are defined under this branch.')
mibBuilder.exportSymbols("CTRON-SSR-SMI-MIB", ssr=ssr, PYSNMP_MODULE_ID=ssr, ssrTraps=ssrTraps, ssrMibs=ssrMibs)
