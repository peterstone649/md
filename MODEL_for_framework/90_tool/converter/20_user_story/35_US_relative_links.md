# User Story: Ensure Clickable Links are Relative

**User Story ID:** US_MFW_35  
**Title:** Ensure Clickable Links are Relative in Generated Documentation  
**Priority:** HIGH  
**Status:** DRAFT  
**Created:** 2026-02-01  
**Last Modified:** 2026-02-01  

## User Story Statement

As a content creator generating documentation with clickable links, I want all generated links to use relative paths instead of absolute paths, so that the documentation remains portable and works correctly when moved to different locations or deployed to different environments.

## User Scenarios

### Scenario 1: Portable Documentation
- **Given** a user generates index files with clickable links
- **When** the documentation is moved to a different directory or server
- **Then** all links should continue to work without requiring path updates

### Scenario 2: Cross-Platform Compatibility
- **Given** documentation is generated on one operating system
- **When** it's accessed on a different operating system
- **Then** relative links should work regardless of the file system structure

### Scenario 3: Deployment Flexibility
- **Given** documentation needs to be deployed to different web servers
- **When** the base URL changes (e.g., from local development to production)
- **Then** relative links should automatically adapt without manual intervention

## Requirements

### Functional Requirements

- **[FR-35-001]**: Index generator MUST create relative links for all file references
- **[FR-35-002]**: HTML converter MUST convert absolute paths to relative paths in generated links
- **[FR-35-003]**: All generated index files MUST use relative paths for internal navigation
- **[FR-35-004]**: Link generation MUST calculate relative paths based on current file location
- **[FR-35-005]**: System MUST handle nested directory structures correctly with relative links
- **[FR-35-006]**: Generated links MUST work when documentation is moved as a complete unit

### Non-Functional Requirements

- **[NFR-35-001]**: Link generation MUST be efficient and not significantly impact performance
- **[NFR-35-002]**: Relative path calculation MUST handle edge cases (empty directories, root level)
- **[NFR-35-003]**: Generated links MUST be valid and testable for correctness
- **[NFR-35-004]**: System MUST maintain backward compatibility with existing relative link structures

## Acceptance Criteria

### AC-35-001: Basic Relative Link Generation
- **Given** an index file is generated in a subdirectory
- **When** links to sibling files are created
- **Then** links use relative paths (e.g., `../sibling.md` instead of `/absolute/path/sibling.md`)

### AC-35-002: Nested Directory Handling
- **Given** documentation with multiple nested levels
- **When** index files are generated at different levels
- **Then** all links use appropriate relative paths (e.g., `../../parent/file.md`)

### AC-35-003: Cross-Tool Consistency
- **Given** both index_generator.py and converter_for_md_to_html.py are used
- **When** they generate links to the same files
- **Then** both tools produce consistent relative link formats

### AC-35-004: Portability Verification
- **Given** documentation with relative links is moved to a new location
- **When** links are tested in the new location
- **Then** all internal links continue to work correctly

## Implementation Notes

### Current Behavior
- Some tools may generate absolute paths
- Link generation may not be consistent across different tools
- No standardized approach for relative path calculation

### Desired Behavior
- All generated links use relative paths
- Consistent relative path format across all tools
- Proper handling of directory traversal (../ notation)
- Cross-platform compatible path separators

### Technical Considerations
- Must integrate with existing path calculation logic
- Should handle both Windows and Unix-style path separators
- Needs to work with the ManagerForDirOTBase for consistent output paths
- Must maintain existing functionality while adding relative link support

## Testing Strategy

### Unit Tests
- Test relative path calculation for various directory structures
- Verify cross-platform path separator handling
- Test edge cases (root directory, single files, deeply nested structures)

### Integration Tests
- Test index_generator.py with relative links
- Test converter_for_md_to_html.py with relative links
- Verify consistency between different tools

### Portability Tests
- Move generated documentation to different locations
- Test link functionality in new locations
- Verify cross-platform compatibility

## Dependencies

- **[DEPENDENCY-35-001]**: ManagerForDirOTBase path handling
- **[DEPENDENCY-35-002]**: Existing index generation logic
- **[DEPENDENCY-35-003]**: HTML conversion path processing
- **[DEPENDENCY-35-004]**: Cross-platform path utilities

## Risk Assessment

- **[RISK-35-001]**: Breaking existing absolute link functionality
  - **Mitigation**: Maintain backward compatibility during transition
- **[RISK-35-002]**: Incorrect relative path calculation in complex structures
  - **Mitigation**: Comprehensive testing with various directory structures
- **[RISK-35-003]**: Cross-platform path separator issues
  - **Mitigation**: Use platform-agnostic path handling utilities

## Stakeholders

- **Primary**: Content creators, Documentation teams, Developers
- **Secondary**: End users accessing documentation, System administrators
- **Approver**: Framework Steward

## Related Artifacts

- **[RELATED-35-001]**: index_generator.py - Index file generation with relative links
- **[RELATED-35-002]**: converter_for_md_to_html.py - HTML conversion with relative links
- **[RELATED-35-003]**: ManagerForDirOTBase - Path management utilities
- **[RELATED-35-004]**: Existing user stories for link generation

## Implementation Priority

1. **Phase 1**: Update index_generator.py for relative links
2. **Phase 2**: Update converter_for_md_to_html.py for relative links
3. **Phase 3**: Add comprehensive testing and validation
4. **Phase 4**: Documentation and migration guide

**User Story Steward:** Framework Steward  
**Approval Status:** Pending  
**Review Cycle:** As needed