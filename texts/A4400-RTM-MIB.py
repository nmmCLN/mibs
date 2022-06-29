#
# PySNMP MIB module A4400-RTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-RTM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:59 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
a4400CPU, = mibBuilder.importSymbols("A4400-CPU-MIB", "a4400CPU")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, NotificationType, Gauge32, ModuleIdentity, ObjectIdentity, iso, Integer32, Unsigned32, MibIdentifier, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "MibIdentifier", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipDomainTable = MibTable((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDomainTable.setStatus('current')
if mibBuilder.loadTexts: ipDomainTable.setDescription('Table for IP Domains.')
ipDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1), ).setMaxAccess("readonly").setIndexNames((0, "A4400-RTM-MIB", "ipDomain"))
if mibBuilder.loadTexts: ipDomainEntry.setStatus('current')
ipDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDomain.setStatus('current')
if mibBuilder.loadTexts: ipDomain.setDescription('IP Domain number as found in MAO.')
confAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: confAvailable.setStatus('current')
if mibBuilder.loadTexts: confAvailable.setDescription('Conference circuits available for given IP Domain')
confBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: confBusy.setStatus('current')
if mibBuilder.loadTexts: confBusy.setDescription('Conference circuits busy for given IP Domain')
confOutOfOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: confOutOfOrder.setStatus('current')
if mibBuilder.loadTexts: confOutOfOrder.setDescription('Conference circuits out of order for given IP Domain')
dspRessAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dspRessAvailable.setStatus('current')
if mibBuilder.loadTexts: dspRessAvailable.setDescription('Compressors available for given IP Domain')
dspRessBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dspRessBusy.setStatus('current')
if mibBuilder.loadTexts: dspRessBusy.setDescription('Compressors busy for given IP Domain')
dspRessOutOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dspRessOutOfService.setStatus('current')
if mibBuilder.loadTexts: dspRessOutOfService.setDescription('Compressors out of order for given IP Domain')
dspRessOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dspRessOverrun.setStatus('current')
if mibBuilder.loadTexts: dspRessOverrun.setDescription('Cumulated compressors overrun for given IP Domain')
cacAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacAllowed.setStatus('current')
if mibBuilder.loadTexts: cacAllowed.setDescription('Number of allowed external communications for given IP Domain')
cacUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacUsed.setStatus('current')
if mibBuilder.loadTexts: cacUsed.setDescription('Current number of external communications for given IP Domain')
cacOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacOverrun.setStatus('current')
if mibBuilder.loadTexts: cacOverrun.setDescription('Cumulated CAC overrun since system startup for given IP Domain')
pbxRole = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("INDETERMINATE", 0), ("MAIN", 1), ("STAND-BY", 2), ("ACTIVE-PCS", 3), ("INACTIVE-PCS", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxRole.setStatus('current')
if mibBuilder.loadTexts: pbxRole.setDescription('The PBX role.')
sipRegSets = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipRegSets.setStatus('current')
if mibBuilder.loadTexts: sipRegSets.setDescription('Registered SIP sets.')
sipUnregSets = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUnregSets.setStatus('current')
if mibBuilder.loadTexts: sipUnregSets.setDescription('Unregistered SIP sets.')
setsInService = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: setsInService.setStatus('current')
if mibBuilder.loadTexts: setsInService.setDescription('Number of sets in service.')
setsOutOfService = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: setsOutOfService.setStatus('current')
if mibBuilder.loadTexts: setsOutOfService.setDescription('Number of sets out of service.')
trunkTable = MibTable((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: trunkTable.setStatus('current')
if mibBuilder.loadTexts: trunkTable.setDescription('Table for Trunks.')
trunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1), ).setMaxAccess("readonly").setIndexNames((0, "A4400-RTM-MIB", "trunkid"))
if mibBuilder.loadTexts: trunkEntry.setStatus('current')
trunkid = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trunkid.setStatus('current')
if mibBuilder.loadTexts: trunkid.setDescription('Trunk number as found in MAO.')
trunkname = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trunkname.setStatus('current')
if mibBuilder.loadTexts: trunkname.setDescription('Name of the Trunk as found in MAO.')
crystalno = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crystalno.setStatus('current')
if mibBuilder.loadTexts: crystalno.setDescription('Crystal number as found in MAO')
couplerno = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: couplerno.setStatus('current')
if mibBuilder.loadTexts: couplerno.setDescription('Coupler number as found in MAO')
trunktype = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("BCA", 0), ("T2", 1), ("T2COMP", 2), ("T2IP", 3), ("T2ATM", 4), ("T2BBC2", 5), ("T2SIP", 6), ("T2IPPR", 7), ("T2", 8), ("MIXTE", 9), ("T0", 10), ("DPNSS", 11), ("DASS2", 12), ("BCAADDON", 13), ("T2HYBRID", 14), ("LIALDE", 15), ("T1", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trunktype.setStatus('current')
if mibBuilder.loadTexts: trunktype.setDescription('Type of the Trunk as found in MAO')
nodepbx = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodepbx.setStatus('current')
if mibBuilder.loadTexts: nodepbx.setDescription('Node number where the trunk exists')
freechan = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freechan.setStatus('current')
if mibBuilder.loadTexts: freechan.setDescription('Available free channnels for given Trunk')
busychan = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busychan.setStatus('current')
if mibBuilder.loadTexts: busychan.setDescription('Used (Busy) channnels for given Trunk')
ooschan = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ooschan.setStatus('current')
if mibBuilder.loadTexts: ooschan.setDescription('Out Of Service channnels for given Trunk')
trunkstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("OOS", 0), ("INS", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trunkstatus.setStatus('current')
if mibBuilder.loadTexts: trunkstatus.setDescription('Status of the trunk group.')
cumuloos = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cumuloos.setStatus('current')
if mibBuilder.loadTexts: cumuloos.setDescription('Cummulated Number of OOS Channels')
cumuloverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 9, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cumuloverrun.setStatus('current')
if mibBuilder.loadTexts: cumuloverrun.setDescription('Cumulated Number of failed outgoing calls (oos/hs)')
mibBuilder.exportSymbols("A4400-RTM-MIB", busychan=busychan, crystalno=crystalno, confAvailable=confAvailable, trunkEntry=trunkEntry, cacAllowed=cacAllowed, pbxRole=pbxRole, cacOverrun=cacOverrun, ipDomainTable=ipDomainTable, dspRessBusy=dspRessBusy, dspRessOverrun=dspRessOverrun, sipRegSets=sipRegSets, trunkTable=trunkTable, couplerno=couplerno, dspRessAvailable=dspRessAvailable, cacUsed=cacUsed, sipUnregSets=sipUnregSets, ipDomain=ipDomain, trunktype=trunktype, trunkid=trunkid, cumuloos=cumuloos, setsInService=setsInService, setsOutOfService=setsOutOfService, ipDomainEntry=ipDomainEntry, trunkstatus=trunkstatus, nodepbx=nodepbx, freechan=freechan, dspRessOutOfService=dspRessOutOfService, confBusy=confBusy, cumuloverrun=cumuloverrun, confOutOfOrder=confOutOfOrder, ooschan=ooschan, trunkname=trunkname)
