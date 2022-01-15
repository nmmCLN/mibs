#
# PySNMP MIB module NET-SNMP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-TC
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:31 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
netSnmpAgentOIDs, netSnmpModuleIDs, netSnmpDomains = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpAgentOIDs", "netSnmpModuleIDs", "netSnmpDomains")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, IpAddress, Counter64, Bits, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Opaque, Counter32, MibIdentifier, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "Bits", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Opaque", "Counter32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpTCs = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 1))
netSnmpTCs.setRevisions(('2002-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpTCs.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: netSnmpTCs.setLastUpdated('200510140000Z')
if mibBuilder.loadTexts: netSnmpTCs.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpTCs.setContactInfo('postal:   Wes Hardaker\n                    P.O. Box 382\n                    Davis CA  95617\n\n          email:    net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpTCs.setDescription('Textual conventions and enumerations for the Net-SNMP project')
class Float(TextualConvention, Opaque):
    description = "A single precision floating-point number.  The semantics\n         and encoding are identical for type 'single' defined in\n         IEEE Standard for Binary Floating-Point,\n         ANSI/IEEE Std 754-1985.\n         The value is restricted to the BER serialization of\n         the following ASN.1 type:\n             FLOATTYPE ::= [120] IMPLICIT FloatType\n         (note: the value 120 is the sum of '30'h and '48'h)\n         The BER serialization of the length for values of\n         this type must use the definite length, short\n         encoding form.\n\n         For example, the BER serialization of value 123\n         of type FLOATTYPE is '9f780442f60000'h.  (The tag\n         is '9f78'h; the length is '04'h; and the value is\n         '42f60000'h.) The BER serialization of value\n         '9f780442f60000'h of data type Opaque is\n         '44079f780442f60000'h. (The tag is '44'h; the length\n         is '07'h; and the value is '9f780442f60000'h.)"
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

hpux9 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 1))
sunos4 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 2))
solaris = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 3))
osf = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 4))
ultrix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 5))
hpux10 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 6))
netbsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 7))
freebsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 8))
irix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 9))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 10))
bsdi = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 11))
openbsd = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 12))
win32 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 13))
hpux11 = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 14))
aix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 15))
macosx = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 16))
dragonfly = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 17))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 2, 255))
netSnmpTCPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 1))
netSnmpUnixDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 2))
netSnmpAAL5PVCDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 3))
netSnmpUDPIPv6Domain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 4))
netSnmpTCPIPv6Domain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 5))
netSnmpCallbackDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 6))
netSnmpAliasDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 7))
netSnmpDTLSUDPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 8))
netSnmpDTLSSCTPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 9))
netSnmpTLSTCPDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 3, 10))
mibBuilder.exportSymbols("NET-SNMP-TC", dragonfly=dragonfly, netSnmpUnixDomain=netSnmpUnixDomain, linux=linux, netSnmpTLSTCPDomain=netSnmpTLSTCPDomain, netSnmpCallbackDomain=netSnmpCallbackDomain, bsdi=bsdi, irix=irix, netSnmpDTLSSCTPDomain=netSnmpDTLSSCTPDomain, solaris=solaris, netbsd=netbsd, netSnmpTCPIPv6Domain=netSnmpTCPIPv6Domain, hpux11=hpux11, aix=aix, netSnmpAliasDomain=netSnmpAliasDomain, hpux9=hpux9, netSnmpDTLSUDPDomain=netSnmpDTLSUDPDomain, PYSNMP_MODULE_ID=netSnmpTCs, hpux10=hpux10, netSnmpAAL5PVCDomain=netSnmpAAL5PVCDomain, ultrix=ultrix, netSnmpTCPDomain=netSnmpTCPDomain, osf=osf, Float=Float, netSnmpUDPIPv6Domain=netSnmpUDPIPv6Domain, macosx=macosx, freebsd=freebsd, netSnmpTCs=netSnmpTCs, sunos4=sunos4, win32=win32, openbsd=openbsd, unknown=unknown)
