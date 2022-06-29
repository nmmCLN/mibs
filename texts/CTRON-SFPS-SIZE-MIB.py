#
# PySNMP MIB module CTRON-SFPS-SIZE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-SIZE-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsSizeService, sfpsSizeServiceAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsSizeService", "sfpsSizeServiceAPI")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sfpsSizeServiceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1), )
if mibBuilder.loadTexts: sfpsSizeServiceTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceTable.setDescription("Displays the current status of the SizeService. This table\n                 displays how much was granted to each user, how much was\n                 requested, the number of times they've requested, the status,\n                 etc. Note :: The <user> refers to the object/code/whatever\n                 which makes a request to the SizeService.")
sfpsSizeServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SIZE-MIB", "sfpsSizeServiceName"))
if mibBuilder.loadTexts: sfpsSizeServiceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceEntry.setDescription('An entry in the SfpsSizeServiceTable instanced by ServiceName')
sfpsSizeServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceName.setDescription("Displays the Name of the SizeService 'user'")
sfpsSizeServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceId.setDescription('Displays the ID corresponding to the Name above')
sfpsSizeServiceElemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceElemSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceElemSize.setDescription('Displays the Element Size for the current user (in bytes).')
sfpsSizeServiceDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceDesired.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceDesired.setDescription('Displays how many Elements/Bytes the current user asked \n                 for in SizeRequest')
sfpsSizeServiceGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceGranted.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceGranted.setDescription('Displays how many Elements/Bytes the current user was \n                 granted via SizeRequest.')
sfpsSizeServiceIncrement = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceIncrement.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceIncrement.setDescription('Displays total Element/Bytes the user was granted via \n                 all IncrementRequest calls.')
sfpsSizeServiceTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceTotalBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceTotalBytes.setDescription('Displays the total number of Bytes the current user was \n                 granted (SizeRequest & IncrementRequest).')
sfpsSizeServiceNbrCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceNbrCalls.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceNbrCalls.setDescription('Displays the number of requests the current user has made \n                 to the SizeService.')
sfpsSizeServiceRtnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("nvramOk", 2), ("unknown", 3), ("notAllowed", 4), ("nonApiOk", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceRtnStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceRtnStatus.setDescription('Displays the Status of the current user.')
sfpsSizeServiceHowGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("elements", 1), ("memory", 2), ("other", 3), ("notAllowed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceHowGranted.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceHowGranted.setDescription("Displays how the current user was granted it's memory.")
sfpsSizeServiceAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("next", 2), ("prev", 3), ("set", 4), ("clear", 5), ("clearAll", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIVerb.setDescription('The action desired to perform on the SizeService Table')
sfpsSizeServiceAPIName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIName.setDescription('Name of the SizeService <user>')
sfpsSizeServiceAPIId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIId.setDescription('ID corresponding to the sfpsSizeServiceAPIName')
sfpsSizeServiceAPIGrant = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIGrant.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIGrant.setDescription('Number of Elements/Bytes being requested via SizeRequest.')
sfpsSizeServiceAPIIncrement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIIncrement.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIIncrement.setDescription('Total Element/Bytes being requested via IncrementRequest')
sfpsSizeServiceAPINumberSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceAPINumberSet.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPINumberSet.setDescription('The Number to set.')
sfpsSizeServiceAPIVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceAPIVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSizeServiceAPIVersion.setDescription('The version.')
mibBuilder.exportSymbols("CTRON-SFPS-SIZE-MIB", sfpsSizeServiceRtnStatus=sfpsSizeServiceRtnStatus, sfpsSizeServiceEntry=sfpsSizeServiceEntry, sfpsSizeServiceAPIVerb=sfpsSizeServiceAPIVerb, sfpsSizeServiceNbrCalls=sfpsSizeServiceNbrCalls, sfpsSizeServiceElemSize=sfpsSizeServiceElemSize, sfpsSizeServiceAPIGrant=sfpsSizeServiceAPIGrant, sfpsSizeServiceName=sfpsSizeServiceName, sfpsSizeServiceDesired=sfpsSizeServiceDesired, sfpsSizeServiceAPINumberSet=sfpsSizeServiceAPINumberSet, sfpsSizeServiceGranted=sfpsSizeServiceGranted, sfpsSizeServiceId=sfpsSizeServiceId, sfpsSizeServiceTable=sfpsSizeServiceTable, sfpsSizeServiceIncrement=sfpsSizeServiceIncrement, sfpsSizeServiceAPIVersion=sfpsSizeServiceAPIVersion, sfpsSizeServiceHowGranted=sfpsSizeServiceHowGranted, sfpsSizeServiceAPIId=sfpsSizeServiceAPIId, sfpsSizeServiceTotalBytes=sfpsSizeServiceTotalBytes, sfpsSizeServiceAPIName=sfpsSizeServiceAPIName, sfpsSizeServiceAPIIncrement=sfpsSizeServiceAPIIncrement)
