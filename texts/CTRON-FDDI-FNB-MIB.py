#
# PySNMP MIB module CTRON-FDDI-FNB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FDDI-FNB-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:45 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ctFDDIFnb, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFDDIFnb")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, IpAddress, ObjectIdentity, Counter64, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "MibIdentifier", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFDDIResource = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1))
ctFDDINonMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2))
ctFDDIMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3))
ctFDDISerialConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4))
ctFDDIResourceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1), )
if mibBuilder.loadTexts: ctFDDIResourceTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceTable.setDescription('This table specifies the physical resources\n                associated with the FNB and general FNB operation for a \n                particular module in a particular slot.')
ctFDDIResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIResourceID"))
if mibBuilder.loadTexts: ctFDDIResourceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceEntry.setDescription('Defines a specific physical resource entry')
ctFDDIResourceSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceSlotID.setDescription('A specific instance of a slot as defined by chSlotID\n                as defined in the chassis MIB.')
ctFDDIResourceID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceID.setDescription('A unique index that defines a specific physcial resource for\n                which this relationship exists.  The value of this is as\n                defined by chResourceID in the chassis MIB.')
ctFDDIResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceType.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceType.setDescription('Defines the type of resource.  This is the same value as\n                chResourceType in the chassis MIB.')
ctFDDIResourceNumbInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIResourceNumbInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResourceNumbInstance.setDescription("This object defines the number of instances of a physical\n                resource.\n\n                Specific resource instances are physically located from \n                top-to-bottom on a particular module. If there are multiple \n                'columns' of a resource from the top to the bottom, then \n                the numbering will start from the left side and proceed \n                top-to-bottom in each column.\n\n                For instance, the first FNB ring will be instance 1 (top \n                in the chassis) while the second FNB ring is instance 2 \n                (below FNB 1 in the backplane).")
ctFDDINonMuxCapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: ctFDDINonMuxCapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxCapTable.setDescription('This table describes all possible capabilities/configurations\n                for all non-muxed FDDI configurations within the chassis.')
ctFDDINonMuxCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConfigID"))
if mibBuilder.loadTexts: ctFDDINonMuxCapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxCapEntry.setDescription('Describes a particular capability/configuration entry.')
ctFDDINMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMSlot.setDescription('The slot within the chassis for which this \n                configuration information is defined.')
ctFDDINMConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfigID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMConfigID.setDescription('The instance of a particular configuration.')
ctFDDINMConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMConfig.setDescription("This object defines a specific valid connection\n                configuration.  It will specify the connection state of all \n                resource instances.  If an instance of a resource is\n                not specified, then it is disconnected.\n\n                Each valid configuration is encoded in an ascii string, using \n                a specified format for interpretation.  The connection \n                specifications are in groups of four where each group defines \n                a specific connection configuration.  The terms of a connection\n                group is defined as follows:\n\n                        1st - The resource ID as defined by \n                        ctFDDIResourceID.\n\n                        2nd - A specific instance of the physical \n                        resource.  This will be a value between 1 and \n                        ctFDDIResourceNumbInstance for the particular \n                        resource ID in the first term.  If a resource ID\n                        has more than one specific resource instance, but\n                        the whole resource can be connected, then this \n                        term will have the value '0' to signify all instances \n                        of the resource.\n\n                        3rd - The connection ID for this specific \n                        physical resource.  This value is the same as \n                        ctFDDINMConnectionID, and through the \n                        ctFDDINonMuxConnectionTable maps to a specific\n                        instance of SMT and MAC.\n\n                For example if the value of this object is '1.1.2.2.1.1',\n                then it states that resource 1, instance 1 is connected to \n                connection ID 2 and resource 2, instance 1 is connected to \n                connection ID 1 and is inserted into its FDDI ring.\n\n                If a valid configuration is no connections then this \n                object will have a value of '0.0.0'")
ctFDDINMConfigDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConfigDesc.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMConfigDesc.setDescription('This object contains a textual description of a valid \n                connection configuration.  This is a more user-friendly \n                representation of the configuration than the ctFDDINMConfig\n                object.')
ctFDDINonMuxCapEnableTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2), )
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableTable.setDescription('This table describes the currently enabled configuration\n                for each module.')
ctFDDINonMuxCapEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMEnableSlot"))
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxCapEnableEntry.setDescription('Describes a specific configuration enable entry.')
ctFDDINMEnableSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMEnableSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMEnableSlot.setDescription('A specific slot for which this configuration enable\n                pertains.')
ctFDDINMCapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDINMCapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMCapEnable.setDescription('A specific configuration that is enabled.  \n\n                Enabling a configuration is done by writing the value of \n                ctFDDINMConfigID for a specific configuration to this object.\n\n                This object, when read, will return the value of \n                ctFDDINMConfigID for the presently enabled configuration.')
ctFDDINonMuxConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3), )
if mibBuilder.loadTexts: ctFDDINonMuxConnectionTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxConnectionTable.setDescription('This table defines specific information for each defined\n                FDDI/FNB connection.  This maps the third sub identifier \n                of ctFDDINMConfig to a particular SMT and MAC instance in\n                the 1512 FDDI MIB.')
ctFDDINonMuxConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDINMConnectionID"))
if mibBuilder.loadTexts: ctFDDINonMuxConnectionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxConnectionEntry.setDescription('Defines a specific configuration connection entry.')
ctFDDINMConnectionSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConnectionSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMConnectionSlot.setDescription('A specific slot for which this connection entry is\n                defined.')
ctFDDINMConnectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMConnectionID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMConnectionID.setDescription('Describes a specific connection identifier.  Valid\n                connection identifiers are defined by the third\n                sub-identifier in ctFDDINMConfig as identified by\n                ctFDDINMCapEnable.')
ctFDDINMSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMSMT.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibSMTIndex')
if mibBuilder.loadTexts: ctFDDINMSMT.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMSMT.setDescription('A specific instance of SMT for which this entry pertains.')
ctFDDINMMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMMAC.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibMACIndex')
if mibBuilder.loadTexts: ctFDDINMMAC.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMMAC.setDescription('A specific MAC that this connection entry pertains.')
ctFDDINMBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMBytes.setDescription('The bandwidth utilization in bytes per second.')
ctFDDINMFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMFrames.setDescription('The bandwidth utilization in frames per second.')
ctFDDINonMuxInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4), )
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceTable.setDescription('This table describs the number of interfaces defined by\n                each non multiplexing FDDI FNB module.')
ctFDDINonMuxInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDINMInterSlot"))
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINonMuxInterfaceEntry.setDescription('A specfic non multiplexing module interface definition.')
ctFDDINMInterSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMInterSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMInterSlot.setDescription('A specific slot for which this inteface entry is\n                defined.')
ctFDDINMNumbInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINMNumbInterfaces.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINMNumbInterfaces.setDescription('The number of interfaces defined on this particular\n                module.')
ctFDDIMuxCapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1), )
if mibBuilder.loadTexts: ctFDDIMuxCapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxCapTable.setDescription('This table describes all possible configuration/capabilities\n                defined for a FDDI multiplexing module.')
ctFDDIMuxCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxConfig"))
if mibBuilder.loadTexts: ctFDDIMuxCapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxCapEntry.setDescription('Describes a specfic FDDI multiplexor capability/configuration\n                entry.')
ctFDDIMuxSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxSlot.setDescription('Defines the slot within the chassis for which this\n                multiplexed capability/configuration entry pertains.')
ctFDDIMuxConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfigID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxConfigID.setDescription('The instance of a particular configuration.')
ctFDDIMuxConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxConfig.setDescription("This object defines a specific valid connection\n                configuration.  It will specify the connection state of all\n                resource instances.  If an instance of a resource is\n                not specified, then it is disconnected.\n\n                Each valid configuration is encoded in an ascii string, using\n                a specified format for interpretation.  The specific \n                connections are in groups of four where each group defines a \n                specific connection configuration.  The terms of the connection \n                group are defined as follows:\n\n                        1st - Resource ID.  The value is the same as \n                        ctFDDIResourceID for a specific resource entry.\n\n                        2nd - Instance of the resource.  This has a value in\n                        the range of 1 to ctFDDIResourceNumbInstance.\n\n                        3rd - Path of the resource as input to the\n                        multiplexor.  Paths are specified as 1\n                        for the primary ring and 2 for the secondary.\n\n                        4th - This is the multiplexor output channel \n                        that this resource comes out of the multiplexor.\n                        This value is the same as a value of ctFDDIMuxOutID.\n\n                        5th - Ring Connectivity.  This sub-identifier\n                        describes if the given mux-in resource \n                        (sub-identifiers 1-3) is inserted into the backplane\n                        FNB ring.  Valid values are 0 for no 1 for yes.\n\n                So for example a value of 1.1.1.1.0.2.2.2.2.1 is resource 1,\n                instance 1 (primary) is on mux-out 1 and it's not inserted;\n                resource 2, instance 2 (secondary) is on mux-out 2 and\n                is inserted into the backplane.\n\n                If a valid configuration is no connections then this\n                object will have a value of '0.0.0.0.0'")
ctFDDIMuxConfigDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxConfigDesc.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxConfigDesc.setDescription('This object contains a textual description of a valid \n                connection configuration.  This is a more user-friendly\n                representation of the configuration than the ctFDDIMuxConfig\n                object.')
ctFDDIMuxCapEnableTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2), )
if mibBuilder.loadTexts: ctFDDIMuxCapEnableTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxCapEnableTable.setDescription('This table describes the currently enabled configuration\n                for each module.')
ctFDDIMuxCapEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxEnableSlot"))
if mibBuilder.loadTexts: ctFDDIMuxCapEnableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxCapEnableEntry.setDescription('Describes a specific configuration enable entry.')
ctFDDIMuxEnableSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxEnableSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxEnableSlot.setDescription('A specific slot for which this configuration enable\n                pertains.')
ctFDDIMuxCapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIMuxCapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxCapEnable.setDescription('A specific instance of the configuration that is\n                enabled.\n\n                Setting this object with a specific value of ctFDDIMuxConfigID\n                enabled that configuration.  A request of the value of this\n                object will return the value of ctFDDIMuxConfigID for the\n                presently enabled configuration.')
ctFDDIMuxMasterPortAssignmentChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignmentChange.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignmentChange.setDescription('Depicts the number of changes to the master port to multiplexor\n                output mapping.')
ctFDDIMuxOutTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3), )
if mibBuilder.loadTexts: ctFDDIMuxOutTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutTable.setDescription('Describes the multiplexor outputs for each of the\n                FNB multiplexor modules.  This maps the multiplexor output\n                to a specific instance of MAC and SMT in the FDDI MIB.')
ctFDDIMuxOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutSlot"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxOutID"))
if mibBuilder.loadTexts: ctFDDIMuxOutEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutEntry.setDescription('Describes a particular multiplexor output.')
ctFDDIMuxOutSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutSlot.setDescription('The given slot for which this multiplexor output information\n                pertains.')
ctFDDIMuxOutID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutID.setDescription('The specific instance of the multiplexor output.  Instances\n                of this object are used by the values of ctFDDIMuxConfig.')
ctFDDIMuxOutMACIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutMACIndex.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibMACIndex')
if mibBuilder.loadTexts: ctFDDIMuxOutMACIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutMACIndex.setDescription('The MAC instance of this multiplexor output.  If this\n                this object has a value greater than 0, then this \n                value is the same as fddimibMACIndex.  If this object has the \n                value of 0, the given mux-out does not have a MAC.')
ctFDDIMuxOutSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxOutSMTIndex.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibSMTIndex')
if mibBuilder.loadTexts: ctFDDIMuxOutSMTIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxOutSMTIndex.setDescription('Identifies the instance of SMT as defined within the\n                FDDI MIB.')
ctFDDIMuxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxBytes.setDescription('The bandwidth utilization in bytes per second.')
ctFDDIMuxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxFrames.setDescription('The bandwidth utilization in frames per second.')
ctFDDIMuxMasterPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4), )
if mibBuilder.loadTexts: ctFDDIMuxMasterPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortTable.setDescription('A list of entries that define master ports as they are\n                defined for the given multiplexed FDDI connection.')
ctFDDIMuxMasterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFDDIMuxMasterPortID"))
if mibBuilder.loadTexts: ctFDDIMuxMasterPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortEntry.setDescription('A specific FDDI-FNB multiplexed master port definition.')
ctFDDIMuxMasterPortSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortSlotID.setDescription('A specific instance of a slot as defined by chSlotID.')
ctFDDIMuxMasterPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortID.setDescription('A unique identifier for this specific master port.')
ctFDDIMuxMasterPortAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignment.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortAssignment.setDescription('Provides the masterport to multiplexor output mapping.\n                This is as defined by ctFDDIMuxOutMacAssignment.')
ctFDDIMuxMasterPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIMuxMasterPortIndex.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibPORTIndex')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIMuxMasterPortIndex.setDescription('Defines a specific port within the FDDI MIBs fddimibPORTTable.')
ctFDDINumbModules = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINumbModules.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINumbModules.setDescription('Describes the number of modules that are present configurable\n                thru the serial control portion of this MIB.\n\n                This directly reflects the number of rows found within the\n                ctFDDISerialConfigTable.')
ctFDDISerialConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2), )
if mibBuilder.loadTexts: ctFDDISerialConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISerialConfigTable.setDescription('This table describes the adminstrative control over each\n                of the FNB serial control modules.')
ctFDDISerialConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFDDISerialSlotID"))
if mibBuilder.loadTexts: ctFDDISerialConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISerialConfigEntry.setDescription('Describes the controls over a single FNB serial control\n                entry.')
ctFDDISerialSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISerialSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISerialSlotID.setDescription('Defines the slot that this FNB serial control module is in.\n                 This is an instance of chSlotID as defined in the chassis MIB.')
ctFDDISerialAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("insertFNB1", 1), ("insertFNB2", 2), ("insertFNB1FNB2", 3), ("bypass", 4), ("hwControlFNB1", 5), ("hwControlFNB2", 6), ("hwControl", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDISerialAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISerialAdminStatus.setDescription('Describes the adminstrative desired state for this FNB\n                serial control module.\n        \n                        insertFNB1(1) - The serial controlled module should be\n                        inserted into FNB-1 and bypass FNB-2.\n\n                        insertFNB2(2) - The serial contolled module should be\n                        inserted into FNB-2 and bypass FNB-1.\n\n                        insertFNB1FNB2(3) - Insert the serial controlled module\n                        on both FNBs.\n\n                        bypass(4) - Bypass the connection to both FNBs.\n\n                        hwControlFNB1(5) - Use hardware settings for FNB-1.\n\n                        hwControlFNB2(6) - Use hardware settings for FNB-2.\n\n                        hwControl(7) - Use the hardware settings for both\n                        FNBs.')
ctFDDISerialOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("insertFNB1", 1), ("insertFNB2", 2), ("insertFNB1FNB2", 3), ("bypass", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISerialOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISerialOperStatus.setDescription('Describes the operational status of this FDDI serial\n                controlled module.\n\n                        insertFNB1(1) - The serial controlled module is\n                        inserted into FNB-1 and bypassed from FNB-2.\n\n                        insertFNB2(2) - The serial controlled module is\n                        bypassed from FNB-1 and inserted into FNB-2.\n\n                        insertFNB1FNB2(3) - The serial controlled module is\n                        inserted into both FNB-1 and FNB-2.\n\n                        bypass(4) - The serial controlled module is bypassed\n                        from both FNB-1 and FNB-2.')
ctFDDIModuleFPIMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3), )
if mibBuilder.loadTexts: ctFDDIModuleFPIMTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIModuleFPIMTable.setDescription('This table describes the FPIMs that are on the front panel of\n                each FDDI serial control module, if that module supports FPIMs.')
ctFDDIModuleFPIMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1), ).setIndexNames((0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIMSlotID"), (0, "CTRON-FDDI-FNB-MIB", "ctFddiFPIM"))
if mibBuilder.loadTexts: ctFDDIModuleFPIMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIModuleFPIMEntry.setDescription('Describes a single FDDI FPIM on a module.')
ctFddiFPIMSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFddiFPIMSlotID.setDescription('Defines the slot in which this module exists.  This\n                is an instance of chSlotID as found in the chassis MIB.')
ctFddiFPIM = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIM.setStatus('mandatory')
if mibBuilder.loadTexts: ctFddiFPIM.setDescription("Defines the instance of the port for which this definition\n                is made.  Ports are physically located from top-to-bottom on a \n                particular module. If there are multiple 'columns' of ports\n                from the top to the bottom, then the numbering will start \n                from the left side and proceed top-to-bottom in each column.")
ctFddiFPIMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctFddiFPIMStatus.setDescription('Describes the link status of the given FPIM.\n\n                A value of link(1) states that a link is present.\n\n                A value of noLink(2) states that no link is present.\n\n                A value of notSupported(3) means that link status is not \n                supported by this port and is unknown.')
ctFddiFPIMType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1, 4, 3, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFddiFPIMType.setStatus('mandatory')
if mibBuilder.loadTexts: ctFddiFPIMType.setDescription('Describes the type of FPIM as found in ctron-oids.')
mibBuilder.exportSymbols("CTRON-FDDI-FNB-MIB", ctFDDIMuxConfig=ctFDDIMuxConfig, ctFDDIMuxMasterPortEntry=ctFDDIMuxMasterPortEntry, ctFDDINMConfigID=ctFDDINMConfigID, ctFDDIMuxCapTable=ctFDDIMuxCapTable, ctFDDINMSlot=ctFDDINMSlot, ctFDDINMEnableSlot=ctFDDINMEnableSlot, ctFDDISerialConfig=ctFDDISerialConfig, ctFDDINMConfig=ctFDDINMConfig, ctFDDIMuxConfigID=ctFDDIMuxConfigID, ctFDDIResourceEntry=ctFDDIResourceEntry, ctFDDIModuleFPIMTable=ctFDDIModuleFPIMTable, ctFDDINMConnectionID=ctFDDINMConnectionID, ctFDDIMuxCapEnableTable=ctFDDIMuxCapEnableTable, ctFDDIMuxMasterPortSlotID=ctFDDIMuxMasterPortSlotID, ctFDDIMuxEnableSlot=ctFDDIMuxEnableSlot, ctFDDISerialConfigTable=ctFDDISerialConfigTable, ctFDDIResource=ctFDDIResource, ctFDDIMuxOutID=ctFDDIMuxOutID, ctFDDINonMuxCapTable=ctFDDINonMuxCapTable, ctFDDIResourceType=ctFDDIResourceType, ctFDDIResourceSlotID=ctFDDIResourceSlotID, ctFDDINonMuxConnectionEntry=ctFDDINonMuxConnectionEntry, ctFDDIMuxCapEnable=ctFDDIMuxCapEnable, ctFDDIMuxMasterPortAssignment=ctFDDIMuxMasterPortAssignment, ctFDDIMuxMasterPortTable=ctFDDIMuxMasterPortTable, ctFDDISerialSlotID=ctFDDISerialSlotID, ctFDDINonMuxCapEntry=ctFDDINonMuxCapEntry, ctFDDIResourceNumbInstance=ctFDDIResourceNumbInstance, ctFDDIMuxOutTable=ctFDDIMuxOutTable, ctFDDIModuleFPIMEntry=ctFDDIModuleFPIMEntry, ctFddiFPIM=ctFddiFPIM, ctFDDINonMux=ctFDDINonMux, ctFDDINonMuxConnectionTable=ctFDDINonMuxConnectionTable, ctFDDINMFrames=ctFDDINMFrames, ctFDDIMuxOutSlot=ctFDDIMuxOutSlot, ctFDDIMuxMasterPortAssignmentChange=ctFDDIMuxMasterPortAssignmentChange, ctFDDIMuxFrames=ctFDDIMuxFrames, ctFDDIMuxCapEntry=ctFDDIMuxCapEntry, ctFDDIResourceID=ctFDDIResourceID, ctFDDINonMuxInterfaceTable=ctFDDINonMuxInterfaceTable, ctFDDIMuxSlot=ctFDDIMuxSlot, ctFddiFPIMStatus=ctFddiFPIMStatus, ctFDDINonMuxInterfaceEntry=ctFDDINonMuxInterfaceEntry, ctFDDISerialConfigEntry=ctFDDISerialConfigEntry, ctFDDINumbModules=ctFDDINumbModules, ctFDDINMInterSlot=ctFDDINMInterSlot, ctFDDIMuxMasterPortID=ctFDDIMuxMasterPortID, ctFddiFPIMSlotID=ctFddiFPIMSlotID, ctFDDINMCapEnable=ctFDDINMCapEnable, ctFddiFPIMType=ctFddiFPIMType, ctFDDINMBytes=ctFDDINMBytes, ctFDDINMSMT=ctFDDINMSMT, ctFDDINonMuxCapEnableTable=ctFDDINonMuxCapEnableTable, ctFDDINMMAC=ctFDDINMMAC, ctFDDINMConnectionSlot=ctFDDINMConnectionSlot, ctFDDIResourceTable=ctFDDIResourceTable, ctFDDIMuxOutEntry=ctFDDIMuxOutEntry, ctFDDINonMuxCapEnableEntry=ctFDDINonMuxCapEnableEntry, ctFDDIMuxBytes=ctFDDIMuxBytes, ctFDDINMConfigDesc=ctFDDINMConfigDesc, ctFDDIMuxConfigDesc=ctFDDIMuxConfigDesc, ctFDDINMNumbInterfaces=ctFDDINMNumbInterfaces, ctFDDIMux=ctFDDIMux, ctFDDIMuxCapEnableEntry=ctFDDIMuxCapEnableEntry, ctFDDIMuxOutMACIndex=ctFDDIMuxOutMACIndex, ctFDDISerialAdminStatus=ctFDDISerialAdminStatus, ctFDDISerialOperStatus=ctFDDISerialOperStatus, ctFDDIMuxMasterPortIndex=ctFDDIMuxMasterPortIndex, ctFDDIMuxOutSMTIndex=ctFDDIMuxOutSMTIndex)
