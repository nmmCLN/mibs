#
# PySNMP MIB module COLUBRIS-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-LICENSE-MIB.my
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:56 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, MibIdentifier, ModuleIdentity, IpAddress, Counter32, Counter64, Gauge32, NotificationType, Integer32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "Gauge32", "NotificationType", "Integer32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 29))
if mibBuilder.loadTexts: colubrisLicenseMIB.setLastUpdated('200606070000Z')
if mibBuilder.loadTexts: colubrisLicenseMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisLicenseMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisLicenseMIB.setDescription('Colubris Licensing Information MIB.')
colubrisLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1))
coLicenseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1))
coLicenseFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1), )
if mibBuilder.loadTexts: coLicenseFeatureTable.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureTable.setDescription('License information attributes.')
coLicenseFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-LICENSE-MIB", "coLicenseFeatureIndex"))
if mibBuilder.loadTexts: coLicenseFeatureEntry.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureEntry.setDescription('An entry in the coLicenseFeatureTable.\n                 coLicenseFeatureIndex - Uniquely identify a license\n                                         feature in a Colubris product.')
coLicenseFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coLicenseFeatureIndex.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureIndex.setDescription('Uniquely identify a license feature in a\n                 Colubris product.')
coLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureName.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureName.setDescription('Friendly name of the license feature.')
coLicenseFeatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureState.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureState.setDescription('Indicates if the feature is enabled or disabled.')
coLicenseFeatureEndingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureEndingDate.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureEndingDate.setDescription('Indicates the date when the feature will be\n                deactivated. The format of the date is YYYY/MM/DD.')
coLicenseFeatureRemainingDays = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureRemainingDays.setStatus('current')
if mibBuilder.loadTexts: coLicenseFeatureRemainingDays.setDescription('Indicates the number of days when the feature will be\n                deactivated. If the feature is permanent, the value\n                9999 is returned.')
colubrisLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2))
colubrisLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1))
colubrisLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2))
colubrisLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 1, 1)).setObjects(("COLUBRIS-LICENSE-MIB", "colubrisLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisLicenseMIBCompliance = colubrisLicenseMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisLicenseMIBCompliance.setDescription('The compliance statement for the License Information MIB.')
colubrisLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 29, 2, 2, 1)).setObjects(("COLUBRIS-LICENSE-MIB", "coLicenseFeatureName"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureState"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureEndingDate"), ("COLUBRIS-LICENSE-MIB", "coLicenseFeatureRemainingDays"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisLicenseMIBGroup = colubrisLicenseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisLicenseMIBGroup.setDescription('A collection of objects for the license information status.')
mibBuilder.exportSymbols("COLUBRIS-LICENSE-MIB", coLicenseFeatureTable=coLicenseFeatureTable, colubrisLicenseMIBGroups=colubrisLicenseMIBGroups, coLicenseFeatureRemainingDays=coLicenseFeatureRemainingDays, colubrisLicenseMIBConformance=colubrisLicenseMIBConformance, coLicenseGroup=coLicenseGroup, colubrisLicenseMIBCompliances=colubrisLicenseMIBCompliances, colubrisLicenseMIBCompliance=colubrisLicenseMIBCompliance, coLicenseFeatureIndex=coLicenseFeatureIndex, colubrisLicenseMIBGroup=colubrisLicenseMIBGroup, coLicenseFeatureEndingDate=coLicenseFeatureEndingDate, colubrisLicenseMIBObjects=colubrisLicenseMIBObjects, coLicenseFeatureEntry=coLicenseFeatureEntry, PYSNMP_MODULE_ID=colubrisLicenseMIB, colubrisLicenseMIB=colubrisLicenseMIB, coLicenseFeatureName=coLicenseFeatureName, coLicenseFeatureState=coLicenseFeatureState)
