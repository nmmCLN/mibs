#
# PySNMP MIB module FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/FREEBSD-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:22:13 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, NotificationType, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, enterprises, Counter64, Counter32, Unsigned32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "enterprises", "Counter64", "Counter32", "Unsigned32", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FREEBSD-MIB", freeBSDpeople=freeBSDpeople, freeBSDVersion=freeBSDVersion, freeBSDports=freeBSDports, PYSNMP_MODULE_ID=freeBSD, freeBSD=freeBSD, freeBSDpeoplePhk=freeBSDpeoplePhk, freeBSDsrc=freeBSDsrc)
