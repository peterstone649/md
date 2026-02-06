# Wikidata Elements: Items, Properties, and Lexemes

## Overview

This document provides a comprehensive analysis of the core elements that constitute Wikidata's data model: Items, Properties, and Lexemes (including Forms). These elements form the foundation of Wikidata's structured data representation and semantic capabilities.

## Core Data Model Elements

### **1. Items (Q-numbers)**

#### **Definition and Purpose**
- **Items** are the fundamental entities in Wikidata, representing real-world objects, concepts, or abstract ideas
- **Format:** Q followed by a number (e.g., Q42 for Douglas Adams, Q123 for a specific book)
- **Purpose:** Provide stable, language-independent identifiers for entities
- **Uniqueness:** Each item represents exactly one distinct entity

#### **Item Structure**
```
Item: Q12345
├── Labels (multilingual names)
├── Descriptions (multilingual descriptions)
├── Aliases (alternative names)
├── Statements (claims about the item)
└── Sitelinks (connections to Wikipedia articles)
```

#### **Item Types and Categories**

##### **Physical Entities**
- **People:** Q123 (individual persons)
- **Places:** Q60 (cities), Q29 (countries), Q152 (mountains)
- **Organizations:** Q43229 (companies), Q1637706 (universities)
- **Buildings:** Q12345 (specific buildings)

##### **Abstract Concepts**
- **Ideas:** Q12345 (philosophical concepts)
- **Events:** Q12345 (historical events)
- **Theories:** Q12345 (scientific theories)
- **Mathematical Concepts:** Q12345 (mathematical objects)

##### **Creative Works**
- **Books:** Q571 (books in general)
- **Films:** Q11424 (films)
- **Music:** Q2188189 (musical works)
- **Software:** Q7397 (software)

#### **Item Management**

##### **Creation Guidelines**
- **Notability:** Items should represent notable, verifiable entities
- **Uniqueness:** Avoid creating duplicate items for the same entity
- **Naming:** Use clear, descriptive labels
- **Documentation:** Provide comprehensive descriptions and aliases

##### **Quality Control**
- **Verification:** All statements should have reliable sources
- **Consistency:** Maintain consistent formatting and terminology
- **Completeness:** Ensure items have adequate information
- **Maintenance:** Regular review and updates

### **2. Properties (P-numbers)**

#### **Definition and Purpose**
- **Properties** define the attributes, relationships, and characteristics that can be assigned to items
- **Format:** P followed by a number (e.g., P31 for "instance of", P27 for "country of citizenship")
- **Purpose:** Provide structured vocabulary for describing items
- **Relationship:** Properties connect subjects (items) to objects (values)

#### **Property Structure**
```
Property: P123
├── Label (property name)
├── Description (what the property describes)
├── Aliases (alternative names)
├── Data Type (type of value expected)
├── Domain (items that can have this property)
├── Range (types of values this property can have)
└── Constraints (rules for using this property)
```

#### **Property Types and Categories**

##### **Identification Properties**
- **P213:** ISNI (International Standard Name Identifier)
- **P244:** Library of Congress Control Number
- **P214:** Virtual International Authority File (VIAF) ID
- **P1006:** BnF (Bibliothèque nationale de France) ID

##### **Relationship Properties**
- **P27:** Country of citizenship
- **P17:** Country
- **P131:** Located in administrative territorial entity
- **P138:** Named after

##### **Temporal Properties**
- **P569:** Date of birth
- **P570:** Date of death
- **P571:** Inception (start date)
- **P576:** Dissolved, abolished, or demolished (end date)

##### **Quantitative Properties**
- **P2048:** Height
- **P2043:** Width
- **P2049:** Diameter
- **P2067:** Mass

##### **Categorical Properties**
- **P31:** Instance of (what kind of thing it is)
- **P279:** Subclass of
- **P361:** Part of
- **P156:** Follows

#### **Property Data Types**

##### **Basic Data Types**
- **String:** Text values (e.g., names, titles)
- **External ID:** Identifiers from external systems
- **URL:** Web addresses
- **Monolingual text:** Text in a specific language

##### **Structured Data Types**
- **Item:** References to other Wikidata items
- **Quantity:** Numbers with units (e.g., 5 meters)
- **Time:** Dates and times with precision
- **Globe coordinate:** Geographic coordinates

##### **Complex Data Types**
- **Mathematical expression:** Mathematical formulas
- **Musical notation:** Musical scores
- **Tabular data:** Structured data tables
- **Geo-shape:** Geographic shapes and boundaries

#### **Property Constraints and Validation**

##### **Common Constraints**
- **Single value constraint:** Property can only have one value
- **Type constraint:** Values must be of specific type
- **Format constraint:** Values must follow specific format
- **Range constraint:** Values must be within specific range

##### **Quality Assurance**
- **Constraint violations:** Automated detection of constraint breaches
- **Data consistency:** Ensuring logical consistency across properties
- **Source requirements:** Mandatory source requirements for certain properties
- **Regular audits:** Periodic review of property usage

### **3. Lexemes (L-numbers)**

#### **Definition and Purpose**
- **Lexemes** represent words or multi-word expressions in natural language
- **Format:** L followed by a number (e.g., L123 for the word "run")
- **Purpose:** Provide structured representation of linguistic information
- **Scope:** Include words, phrases, idioms, and other lexical units

#### **Lexeme Structure**
```
Lexeme: L123
├── Language (language of the lexeme)
├── Category (part of speech)
├── Lexical category (grammatical category)
├── Statements (claims about the lexeme)
├── Forms (different inflected forms)
└── Senses (different meanings)
```

#### **Lexeme Components**

##### **Lexical Categories**
- **Nouns:** L123 (nouns)
- **Verbs:** L456 (verbs)
- **Adjectives:** L789 (adjectives)
- **Adverbs:** L101 (adverbs)

##### **Language Representation**
- **Language codes:** ISO 639-3 language codes
- **Multilingual support:** Lexemes can exist in multiple languages
- **Translation links:** Connections between lexemes in different languages
- **Language-specific rules:** Grammar and usage rules per language

### **4. Forms (F-numbers)**

#### **Definition and Purpose**
- **Forms** represent different inflected versions of a lexeme
- **Format:** F followed by a number (e.g., F123 for "running" as a form of "run")
- **Purpose:** Capture grammatical variations of words
- **Relationship:** Each form belongs to exactly one lexeme

#### **Form Structure**
```
Form: F123
├── Representation (the actual word form)
├── Grammatical features (grammatical properties)
├── Statements (claims about the form)
└── Lexeme (parent lexeme)
```

#### **Grammatical Features**

##### **Morphological Features**
- **Number:** Singular, plural, dual
- **Case:** Nominative, accusative, genitive, etc.
- **Gender:** Masculine, feminine, neuter
- **Person:** First, second, third person

##### **Tense and Aspect**
- **Tense:** Past, present, future
- **Aspect:** Perfect, imperfect, progressive
- **Mood:** Indicative, imperative, subjunctive
- **Voice:** Active, passive, middle

##### **Other Features**
- **Degree:** Positive, comparative, superlative
- **Form:** Infinitive, participle, gerund
- **Register:** Formal, informal, archaic

## Integration and Relationships

### **Element Interconnections**

#### **Item-Property Relationships**
```
Item (Q123) + Property (P27) + Value (Q142) = Statement
"Paris" + "country" + "France" = "Paris is in France"
```

#### **Lexeme-Form Relationships**
```
Lexeme (L123) + Form (F456) = Inflected form
"run" + "running" = Present participle form
```

#### **Cross-Element Links**
- **Items to Lexemes:** Items can reference lexemes for linguistic information
- **Properties to Items:** Properties can have items as values
- **Lexemes to Items:** Lexemes can reference items for meaning

### **Semantic Relationships**

#### **Hierarchical Relationships**
- **Subclass relationships:** P279 (subclass of)
- **Part-whole relationships:** P361 (part of)
- **Instance relationships:** P31 (instance of)

#### **Associative Relationships**
- **Temporal relationships:** P580 (start time), P582 (end time)
- **Spatial relationships:** P131 (located in), P276 (location)
- **Causal relationships:** P1542 (has effect), P1416 (affiliation)

## Applications and Use Cases

### **Knowledge Representation**

#### **Structured Data Storage**
- **Entity description:** Comprehensive item descriptions
- **Relationship mapping:** Complex relationship networks
- **Multilingual support:** Language-independent data
- **Version control:** Historical data tracking

#### **Semantic Web Integration**
- **RDF export:** Standard semantic web format
- **SPARQL queries:** Complex data querying
- **Linked data:** Integration with external datasets
- **Knowledge graphs:** Semantic network construction

### **Natural Language Processing**

#### **Lexical Resources**
- **Dictionary creation:** Structured lexical databases
- **Grammar analysis:** Grammatical feature extraction
- **Translation support:** Cross-lingual lexical mapping
- **Language learning:** Educational language resources

#### **Computational Linguistics**
- **Corpus annotation:** Automated text annotation
- **Language modeling:** Training data for NLP models
- **Semantic analysis:** Meaning-based text analysis
- **Information extraction:** Structured information from text

### **Research Applications**

#### **Linguistic Research**
- **Language comparison:** Cross-linguistic analysis
- **Grammar studies:** Grammatical feature analysis
- **Lexical semantics:** Word meaning relationships
- **Language evolution:** Historical language changes

#### **Knowledge Organization**
- **Taxonomy creation:** Hierarchical knowledge organization
- **Concept mapping:** Semantic concept relationships
- **Information retrieval:** Enhanced search capabilities
- **Data integration:** Cross-domain data linking

## Quality Assurance and Maintenance

### **Data Quality Standards**

#### **Item Quality**
- **Uniqueness verification:** Preventing duplicate items
- **Source validation:** Reliable source requirements
- **Completeness checks:** Ensuring adequate item information
- **Consistency maintenance:** Uniform data formatting

#### **Property Quality**
- **Definition clarity:** Clear property descriptions
- **Usage consistency:** Consistent property application
- **Constraint enforcement:** Automated constraint checking
- **Documentation completeness:** Comprehensive property documentation

#### **Lexeme Quality**
- **Linguistic accuracy:** Correct grammatical information
- **Language coverage:** Comprehensive language representation
- **Form completeness:** Complete inflectional paradigms
- **Sense clarity:** Clear meaning distinctions

### **Community Maintenance**

#### **Editorial Guidelines**
- **Contribution standards:** Clear contribution guidelines
- **Review processes:** Community review mechanisms
- **Dispute resolution:** Conflict resolution procedures
- **Quality monitoring:** Ongoing quality assessment

#### **Tool Support**
- **Editing tools:** User-friendly editing interfaces
- **Validation tools:** Automated data validation
- **Analysis tools:** Data quality analysis tools
- **Reporting tools:** Quality monitoring reports

## Future Developments

### **Enhanced Capabilities**

#### **Advanced Data Types**
- **Complex structures:** Support for more complex data types
- **Temporal data:** Enhanced temporal data handling
- **Spatial data:** Improved geographic data representation
- **Multimedia data:** Integration of multimedia elements

#### **Improved Quality Control**
- **AI assistance:** AI-powered data validation
- **Automated curation:** Automated data maintenance
- **Enhanced constraints:** More sophisticated constraint systems
- **Quality metrics:** Advanced quality measurement systems

### **Broader Integration**

#### **External Systems**
- **Library systems:** Enhanced library catalog integration
- **Research databases:** Academic database integration
- **Cultural heritage:** Museum and archive integration
- **Government data:** Public sector data integration

#### **User Experience**
- **Mobile access:** Enhanced mobile interfaces
- **Voice interfaces:** Voice-based data access
- **Visual interfaces:** Improved data visualization
- **Accessibility:** Enhanced accessibility features

## Conclusion

Wikidata's elements—Items, Properties, and Lexemes with their Forms—provide a comprehensive framework for structured knowledge representation. This data model enables:

- **Precise entity identification** through unique item identifiers
- **Structured relationship mapping** through well-defined properties
- **Comprehensive linguistic representation** through lexemes and forms
- **Multilingual knowledge organization** through language-independent structures
- **Semantic web integration** through standard data formats and protocols

The combination of these elements creates a powerful foundation for knowledge organization, natural language processing, and semantic web applications, making Wikidata a central hub for structured data on the web.

**Wikidata's data model, built on Items, Properties, and Lexemes with their Forms, provides a comprehensive framework for structured knowledge representation that enables precise entity identification, structured relationship mapping, and comprehensive linguistic representation across multiple languages.**

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|----------------|--------------|------------|
| V1.0.0 | 2026-02-06 | Initial creation of comprehensive Wikidata elements documentation | AI Framework Steward | Document detailed analysis of Wikidata's core elements and their relationships |
