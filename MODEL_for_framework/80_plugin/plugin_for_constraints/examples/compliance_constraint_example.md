# 🏛️ Compliance Constraint Example: Data Protection Standards

**Example constraint definition for GDPR compliance and data protection**

## 📋 Constraint Overview

**Constraint ID**: CP-001
**Constraint Name**: Data Protection Compliance
**Type**: Compliance Constraint
**Enforcement Level**: Critical
**Created**: January 2026
**Owner**: Legal & Compliance Team

## 🎯 What This Constraint Ensures

This constraint ensures that all framework components handling personal data comply with GDPR (General Data Protection Regulation) and other applicable data protection laws. It protects user privacy and ensures legal compliance for data processing activities.

**Why this matters:**
- Avoids significant legal and financial penalties
- Protects user privacy and builds trust
- Ensures consistent data protection practices across the framework
- Demonstrates commitment to ethical data handling

## 📝 Constraint Specification

### Requirements

1. **Data Encryption**: All personal data must be encrypted at rest and in transit
2. **Access Control**: Role-based access control for all data access operations
3. **Data Minimization**: Only collect and process data necessary for specified purposes
4. **Audit Logging**: Complete audit trail for all data access and modifications
5. **Data Subject Rights**: Support for data access, correction, and deletion requests
6. **Data Protection Impact Assessment**: DPIA required for high-risk processing

### Acceptance Criteria

- [ ] All personal data encrypted using approved encryption standards
- [ ] Access control implemented with least privilege principle
- [ ] Data collection limited to necessary fields only
- [ ] Audit logs capture all data access with user identification
- [ ] Data subject request handling process documented and tested
- [ ] DPIA completed for all high-risk data processing activities

### Implementation Details

**Technical Specifications:**
```yaml
data_protection:
  encryption:
    at_rest: "AES-256 encryption"
    in_transit: "TLS 1.3 minimum"
    key_management: "HSM or approved key management service"
  access_control:
    authentication: "Multi-factor authentication required"
    authorization: "Role-based access control (RBAC)"
    principle: "Least privilege access"
  data_handling:
    minimization: "Only necessary data collected"
    retention: "Defined retention periods with automatic deletion"
    purpose_limitation: "Data used only for specified purposes"
  audit_trail:
    coverage: "All data access and modifications"
    retention: "Minimum 7 years"
    integrity: "Tamper-evident logging"
  data_subject_rights:
    access_request: "Process within 30 days"
    correction: "Update within 14 days"
    deletion: "Secure deletion within 30 days"
    portability: "Export in machine-readable format"
```

**Validation Methods:**
- **Automated Scanning**: Regular security scans for encryption and access controls
- **Manual Audits**: Periodic compliance audits and DPIA reviews
- **Documentation Review**: Process documentation and procedure validation
- **User Testing**: Data subject request handling process testing

**Tools & Technologies:**
- **Encryption**: OpenSSL, AWS KMS, Azure Key Vault
- **Access Control**: OAuth 2.0, OpenID Connect, LDAP/Active Directory
- **Audit Logging**: ELK Stack, Splunk, or equivalent SIEM solutions
- **DPIA Tools**: Specialized data protection impact assessment tools
- **Compliance Monitoring**: Automated compliance scanning tools

## 🔄 Enforcement & Monitoring

### Validation Process

**When Checked:**
- **Pre-deployment**: Security and compliance validation in CI/CD
- **Runtime**: Continuous monitoring of access patterns and encryption
- **Regular Audits**: Quarterly compliance audits and annual DPIA reviews
- **Incident Response**: Immediate validation during security incidents

**Who Enforces:**
- **Automated**: Security scanning tools and monitoring systems
- **Manual**: Compliance team and external auditors
- **Legal**: Legal team for regulatory compliance validation

### Monitoring & Reporting

**Compliance Metrics:**
- Encryption coverage percentage for personal data
- Access control violation incidents
- Data minimization compliance score
- Audit log completeness and integrity
- Data subject request response times
- DPIA completion rate for new projects

**Reporting Frequency:**
- **Real-time**: Security incident alerts and access violations
- **Weekly**: Compliance dashboard updates
- **Monthly**: Detailed compliance reports to management
- **Quarterly**: Full compliance audit reports
- **Annually**: Regulatory compliance certification

**Violation Handling:**
- **Encryption failures**: Immediate blocking of data access
- **Access violations**: Account suspension and investigation
- **Audit gaps**: Mandatory remediation within 24 hours
- **DPIA non-compliance**: Project halt until assessment completed

## 📚 Examples

### Compliant Example

```javascript
// Secure data handling implementation
class UserDataProcessor {
  constructor() {
    this.encryptionService = new EncryptionService();
    this.auditLogger = new AuditLogger();
    this.accessControl = new AccessControl();
  }

  async processUserData(userData, purpose) {
    // 1. Validate access permissions
    const hasAccess = await this.accessControl.checkAccess(
      currentUser, 
      'process_personal_data', 
      purpose
    );
    if (!hasAccess) {
      this.auditLogger.logAccessDenied(currentUser, purpose);
      throw new Error('Access denied: insufficient permissions');
    }

    // 2. Encrypt sensitive data
    const encryptedData = this.encryptionService.encrypt(userData);
    
    // 3. Log data access for audit trail
    this.auditLogger.logDataAccess({
      userId: currentUser.id,
      action: 'process_personal_data',
      purpose: purpose,
      timestamp: new Date().toISOString()
    });

    // 4. Process only necessary data fields
    const necessaryFields = this.extractNecessaryFields(encryptedData, purpose);
    const result = await this.performProcessing(necessaryFields);

    return result;
  }

  async handleDataSubjectRequest(request) {
    // Validate request and user identity
    const validated = await this.validateDataSubjectRequest(request);
    if (!validated) {
      throw new Error('Invalid data subject request');
    }

    // Process request based on type
    switch (request.type) {
      case 'access':
        return await this.provideDataAccess(request.userId);
      case 'correction':
        return await this.updateUserData(request.userId, request.updates);
      case 'deletion':
        return await this.deleteUserData(request.userId);
      default:
        throw new Error('Unsupported request type');
    }
  }
}
```

### Non-compliant Example

```javascript
// Insecure data handling - DO NOT USE
class UserDataProcessor {
  async processUserData(userData) {
    // No access control
    // No encryption
    // No audit logging
    // Processing all data fields regardless of need
    
    const result = await this.performProcessing(userData);
    return result;
  }
  
  // No data subject rights implementation
  // No compliance with legal requirements
}
```

**Issues:**
- No encryption of personal data
- No access control or authentication
- No audit trail for data access
- No data minimization
- No support for data subject rights
- No DPIA or compliance documentation

### Best Practices

1. **Data Classification**: Classify data based on sensitivity and apply appropriate protection
2. **Privacy by Design**: Implement data protection from the initial design phase
3. **Regular Training**: Ensure all team members understand data protection requirements
4. **Incident Response**: Have clear procedures for data breaches and security incidents
5. **Documentation**: Maintain comprehensive documentation of data processing activities

## 🔄 Maintenance & Updates

### Review Schedule
- **Monthly**: Review access logs and security metrics
- **Quarterly**: Full compliance audit and DPIA review
- **Annually**: Update based on regulatory changes and framework evolution
- **As needed**: Immediate review after security incidents or regulatory updates

### Update Process
1. **Regulatory Monitoring**: Track changes in data protection laws
2. **Risk Assessment**: Assess impact of regulatory changes on framework
3. **Technical Updates**: Implement necessary technical changes
4. **Process Updates**: Update procedures and documentation
5. **Training Updates**: Update team training materials and sessions

### Impact Assessment

**When Updating This Constraint:**
- **Legal Compliance**: Changes may be required by law
- **Technical Implementation**: May require significant system changes
- **User Experience**: May impact user interface and workflows
- **Performance**: Encryption and logging may impact system performance
- **Cost**: Additional compliance measures may increase operational costs

## 🤝 Stakeholder Information

### Primary Owner
**Owner**: Legal & Compliance Team
**Contact**: compliance@framework.org
**Responsibilities**: Regulatory compliance, DPIA oversight, legal review

### Reviewers
**Technical Reviewer**: Security Team Lead
**Compliance Reviewer**: Data Protection Officer (DPO)
**Legal Reviewer**: Chief Legal Officer

### Affected Teams
- All development teams handling personal data
- Security and IT operations teams
- Legal and compliance teams
- Customer support and data subject request handlers
- Product management and design teams

## 📞 Additional Information

### References
- [GDPR Official Text](https://gdpr.eu/)
- [Framework Data Protection Policy](https://framework.org/data-protection-policy)
- [Security Standards](https://framework.org/security-standards)

### Notes
- This constraint applies to all components handling personal data
- Regular training required for all team members
- External audits may be required for compliance certification

### Related Constraints
- [Security Standards](../constraint_types.md#security-constraints)
- [Process Compliance](../constraint_types.md#compliance-constraints)

---

**Next Steps**: Use this example as a template for defining your own compliance constraints!