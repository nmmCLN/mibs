#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 16:14:01 2022
# On host fv-az208-754 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, TimeTicks, Unsigned32, MibIdentifier, Bits, enterprises, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ModuleIdentity, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "enterprises", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
freeBSD = ModuleIdentity((1, 3, 6, 1, 4, 1, 2238))
freeBSD.setRevisions(('2006-10-31 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: freeBSD.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: freeBSD.setLastUpdated('200610311000Z')
if mibBuilder.loadTexts: freeBSD.setOrganization('The FreeBSD Project.')
if mibBuilder.loadTexts: freeBSD.setContactInfo('phk@FreeBSD.org is contact person for this file.\n\t\t core@FreeBSD.org is the final authority.')
if mibBuilder.loadTexts: freeBSD.setDescription('The Structure of Management Information for the\n\t\tFreeBSD Project enterprise MIB subtree.')
freeBSDsrc = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 1))
if mibBuilder.loadTexts: freeBSDsrc.setStatus('current')
if mibBuilder.loadTexts: freeBSDsrc.setDescription('Subtree for things which lives in the src tree.')
freeBSDports = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 2))
if mibBuilder.loadTexts: freeBSDports.setStatus('current')
if mibBuilder.loadTexts: freeBSDports.setDescription('Subtree for things which lives in the ports tree.')
freeBSDpeople = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3))
if mibBuilder.loadTexts: freeBSDpeople.setStatus('current')
if mibBuilder.loadTexts: freeBSDpeople.setDescription('Subtree for FreeBSD people.\n\t\t Under this branch any FreeBSD committer may claim\n\t\t a subtree.  Grab the next sequential oid in the list.\n\t\t These assignments are not revoked when committers leave\n\t\t the FreeBSD project.\n\t\t')
freeBSDpeoplePhk = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 3, 1))
if mibBuilder.loadTexts: freeBSDpeoplePhk.setStatus('current')
if mibBuilder.loadTexts: freeBSDpeoplePhk.setDescription('Subtree for phk@FreeBSD.org')
freeBSDVersion = ObjectIdentity((1, 3, 6, 1, 4, 1, 2238, 4))
if mibBuilder.loadTexts: freeBSDVersion.setStatus('current')
if mibBuilder.loadTexts: freeBSDVersion.setDescription('Subtree to register FreeBSD versions. The OID for a FreeBSD\n\t\t version is formed by appending the dot delimited numbers\n\t\t from the release number to this base OID. Examples:\n\n\t\t  5.2.1-STABLE:\tfreeBSDVersion.5.2.1\n\t\t  6.1-STABLE:\tfreeBSDVersion.6.1\n\t\t  7.0-CURRENT:\tfreeBSDVersion.7.0\n\n\t\t There is no indication whether this is STABLE or CURRENT.\n\n\t\t The sysObjectId is automatically set to the value indicated\n\t\t by the uname(3) release field by bsnmpd(1). This initial\n\t\t value can be overwritten in the configuration file.')
mibBuilder.exportSymbols("FREEBSD-MIB", freeBSD=freeBSD, freeBSDports=freeBSDports, PYSNMP_MODULE_ID=freeBSD, freeBSDpeople=freeBSDpeople, freeBSDpeoplePhk=freeBSDpeoplePhk, freeBSDsrc=freeBSDsrc, freeBSDVersion=freeBSDVersion)
