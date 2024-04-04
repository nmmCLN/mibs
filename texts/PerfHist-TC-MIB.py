#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:29 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, ModuleIdentity, TimeTicks, IpAddress, NotificationType, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, mib_2, Integer32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ModuleIdentity", "TimeTicks", "IpAddress", "NotificationType", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "mib-2", "Integer32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
perfHistTCMIB.setRevisions(('2003-08-13 00:00', '1998-11-07 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: perfHistTCMIB.setRevisionsDescriptions(('Contact information and references updated.\n       No technical changes have been applied.\n       Published as RFC 3593.', 'The RFC 2493 version of this MIB module.',))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('200308130000Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToM MIB WG')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('WG charter:\n           http://www.ietf.org/html.charters/atommib-charter.html\n\n         Mailing Lists:\n           General Discussion: atommib@research.telcordia.com\n           To Subscribe: atommib-request@research.telcordia.com\n\n         Editor:  Kaj Tesink\n         Postal:  Telcordia Technologies\n                  331 Newman Springs Road\n                  Red Bank, NJ 07701\n                  USA\n         Tel:     +1 732 758 5254\n         E-mail:  kaj@research.telcordia.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions\n       to be used by systems supporting 15 minute\n       based performance history counts.\n\n       Copyright (C) The Internet Society (2003).\n       This version of this MIB module is part of\n       RFC 3593;  see the RFC itself for full\n       legal notices.')
class PerfCurrentCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n          performance measurement in a current 15\n          minute measurement interval.  The value\n          of this counter starts from zero and is\n          increased when associated events occur,\n          until the end of the 15 minute interval.\n          At that time the value of the counter is\n          stored in the first 15 minute history\n          interval, and the CurrentCount is\n          restarted at zero.  In the\n          case where the agent has no valid data\n          available for the current interval the\n          corresponding object instance is not\n          available and upon a retrieval request\n          a corresponding error message shall be\n          returned to indicate that this instance\n          does not exist (for example, a noSuchName\n          error for SNMPv1 and a noSuchInstance for\n          SNMPv2 GET operation).'
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n          performance measurement in a previous\n          15 minute measurement interval.  In the\n          case where the agent has no valid data\n          available for a particular interval the\n          corresponding object instance is not\n          available and upon a retrieval request\n          a corresponding error message shall be\n          returned to indicate that this instance\n          does not exist (for example, a noSuchName\n          error for SNMPv1 and a noSuchInstance for\n          SNMPv2 GET operation).\n          In a system supporting\n          a history of n intervals with\n          IntervalCount(1) and IntervalCount(n) the\n          most and least recent intervals\n          respectively, the following applies at\n          the end of a 15 minute interval:\n          - discard the value of IntervalCount(n)\n          - the value of IntervalCount(i) becomes that\n            of IntervalCount(i-1) for n >= i > 1\n          - the value of IntervalCount(1) becomes that\n            of CurrentCount\n          - the TotalCount, if supported, is adjusted.'
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n          performance measurements aggregating the\n          previous valid 15 minute measurement\n          intervals.  (Intervals for which no valid\n          data was available are not counted)'
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfIntervalCount=PerfIntervalCount, PerfCurrentCount=PerfCurrentCount, PerfTotalCount=PerfTotalCount, perfHistTCMIB=perfHistTCMIB, PYSNMP_MODULE_ID=perfHistTCMIB)
