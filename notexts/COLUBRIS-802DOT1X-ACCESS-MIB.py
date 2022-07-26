#
# PySNMP MIB module COLUBRIS-802DOT1X-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-802DOT1X-MIB.my
# Produced by pysmi-1.1.8 at Tue Jul 26 15:28:56 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, IpAddress, TimeTicks, ModuleIdentity, NotificationType, Gauge32, iso, ObjectIdentity, Counter32, Integer32, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "Gauge32", "iso", "ObjectIdentity", "Counter32", "Integer32", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
colubris802Dot1xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 8))
if mibBuilder.loadTexts: colubris802Dot1xMIB.setLastUpdated('200601090000Z')
if mibBuilder.loadTexts: colubris802Dot1xMIB.setOrganization('Colubris Networks, Inc.')
coPaeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1))
coDot1xPaeSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1))
coDot1xPaeAuthenticator = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2))
coDot1xPaeSystemModifyKey = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKey.setStatus('current')
coDot1xPaeSystemModifyKeyInterval = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKeyInterval.setStatus('current')
coDot1xAuthQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthQuietPeriod.setStatus('current')
coDot1xAuthTxPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthTxPeriod.setStatus('current')
coDot1xAuthSuppTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthSuppTimeout.setStatus('current')
coDot1xAuthServerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthServerTimeout.setStatus('current')
coDot1xAuthMaxReq = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthMaxReq.setStatus('current')
coDot1xAuthReAuthPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthPeriod.setStatus('current')
coDot1xAuthReAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthEnabled.setStatus('current')
coDot1xAuthKeyTxEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthKeyTxEnabled.setStatus('current')
coDot1xAuthReAuthMax = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthMax.setStatus('current')
coDot1xPaeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2))
coDot1xPaeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1))
coDot1xPaeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2))
coDot1xPaeSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 1)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKey"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKeyInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeSystemGroup = coDot1xPaeSystemGroup.setStatus('current')
coDot1xPaeAuthenticatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 2)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthQuietPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthTxPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthSuppTimeout"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthServerTimeout"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthMaxReq"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthEnabled"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthKeyTxEnabled"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeAuthenticatorGroup = coDot1xPaeAuthenticatorGroup.setStatus('current')
coDot1xPaeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2, 1)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemGroup"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeAuthenticatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeCompliance = coDot1xPaeCompliance.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-802DOT1X-ACCESS-MIB", coDot1xPaeSystemGroup=coDot1xPaeSystemGroup, coDot1xAuthMaxReq=coDot1xAuthMaxReq, coDot1xPaeSystem=coDot1xPaeSystem, coDot1xAuthServerTimeout=coDot1xAuthServerTimeout, coDot1xAuthQuietPeriod=coDot1xAuthQuietPeriod, coDot1xPaeAuthenticatorGroup=coDot1xPaeAuthenticatorGroup, coDot1xPaeGroups=coDot1xPaeGroups, PYSNMP_MODULE_ID=colubris802Dot1xMIB, coDot1xPaeConformance=coDot1xPaeConformance, coDot1xPaeSystemModifyKey=coDot1xPaeSystemModifyKey, coDot1xAuthKeyTxEnabled=coDot1xAuthKeyTxEnabled, coPaeMIBObjects=coPaeMIBObjects, coDot1xPaeCompliance=coDot1xPaeCompliance, coDot1xAuthTxPeriod=coDot1xAuthTxPeriod, coDot1xPaeCompliances=coDot1xPaeCompliances, coDot1xAuthReAuthEnabled=coDot1xAuthReAuthEnabled, coDot1xAuthReAuthMax=coDot1xAuthReAuthMax, colubris802Dot1xMIB=colubris802Dot1xMIB, coDot1xPaeAuthenticator=coDot1xPaeAuthenticator, coDot1xPaeSystemModifyKeyInterval=coDot1xPaeSystemModifyKeyInterval, coDot1xAuthReAuthPeriod=coDot1xAuthReAuthPeriod, coDot1xAuthSuppTimeout=coDot1xAuthSuppTimeout)
