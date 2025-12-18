
```markdown
# Security Automation & Forensics Tools

Python security and digital forensics scripts developed during University of Arizona Cyber Operations Engineering program (B.A.S., 3.89 GPA).

## 🛡️ Security Domains Covered

- **Digital Forensics** - Memory analysis, file system forensics, evidence collection
- **Network Security** - Packet capture and socket programming
- **Cryptography** - Password security and hash cracking concepts
- **Web Security** - Web scraping and reconnaissance
- **File Analysis** - Integrity verification and metadata extraction
- **Text Analysis** - Natural language processing and corpus analysis

---

## 📁 Scripts by Category

### Digital Forensics

#### 1. Memory Forensics Analyzer
**File:** `forensics/memory_forensics_analyzer.py`
- **Purpose:** Analyze memory dumps for forensic investigation
- **Techniques:** Chunked file processing, regex pattern matching, keyword extraction
- **Use Case:** Incident response, malware analysis, memory forensics
- **Skills:** File I/O optimization, memory-efficient processing, forensic analysis

#### 2. File Metadata Processor
**File:** `forensics/file_metadata_processor.py`
- **Purpose:** Object-oriented file forensics with comprehensive metadata extraction
- **Techniques:** OOP design, file system analysis, header extraction
- **Use Case:** Digital evidence collection, file system forensics
- **Skills:** Python classes, error handling, forensic documentation

#### 3. Email & URL Extractor
**File:** `forensics/email_url_extractor.py`
- **Purpose:** Extract email addresses and URLs from memory dumps
- **Techniques:** Regular expressions, pattern matching, frequency analysis
- **Use Case:** Investigation of communication artifacts, data exfiltration detection
- **Skills:** Regex mastery, chunked processing, data extraction

#### 4. Memory String Analyzer
**File:** `forensics/memory_string_analyzer.py`
- **Purpose:** Extract and analyze text strings from binary memory dumps
- **Techniques:** String pattern matching, frequency analysis
- **Use Case:** Memory forensics, artifact recovery
- **Skills:** Binary file processing, statistical analysis

#### 5. File Hash Duplicate Detector
**File:** `forensics/file_hash_duplicate_detector.py`
- **Purpose:** Identify duplicate files using MD5 hashing
- **Techniques:** Hash-based deduplication, recursive scanning
- **Use Case:** Storage optimization, forensic duplicate detection
- **Skills:** Hash algorithms, file system traversal

#### 6. System Information Logger
**File:** `forensics/system_info_logger.py`
- **Purpose:** Comprehensive forensic system profiling and file cataloging
- **Techniques:** System metadata collection, SHA-256 hashing, forensic logging
- **Use Case:** Incident response, evidence collection, system baseline
- **Skills:** System profiling, forensic documentation, chain of custody

#### 7. Firewall Log Parser
**File:** `forensics/firewall_log_parser.py`
- **Purpose:** Parse security logs to detect malware signatures
- **Techniques:** Log parsing, pattern matching, threat detection
- **Use Case:** Security monitoring, malware detection, log analysis
- **Skills:** Log analysis, threat intelligence, pattern recognition

#### 8. GPS EXIF Extractor
**File:** `forensics/gps_exif_extractor.py`
- **Purpose:** Extract GPS coordinates and metadata from JPEG images
- **Techniques:** EXIF parsing, coordinate conversion, geolocation analysis
- **Use Case:** Digital forensics, OSINT, tracking evidence locations
- **Skills:** Image metadata extraction, GPS data processing, CSV export
---

### File Analysis

#### 9. File Hash Analyzer
**File:** `file-analysis/file_hash_analyzer.py`
- **Purpose:** Generate forensic catalog of files with SHA-256 integrity hashes
- **Techniques:** Recursive directory walking, cryptographic hashing, timeline analysis
- **Use Case:** File integrity monitoring, baseline security audits, chain of custody
- **Skills:** Cryptographic hashing, file system operations, forensic timelines

#### 10. Image Scanner
**File:** `file-analysis/image_scanner.py`
- **Purpose:** Detect and analyze digital images in directories
- **Techniques:** Image format detection, metadata extraction using PIL
- **Use Case:** Digital evidence discovery, image forensics
- **Skills:** Image processing, file type detection, data presentation

---

### Network Security

#### 11. Packet Sniffer
**File:** `network/packet_sniffer.py`
- **Purpose:** Capture and analyze network traffic
- **Techniques:** Raw socket programming, packet header parsing, protocol identification
- **Use Case:** Network forensics, traffic analysis, intrusion detection
- **Skills:** Socket programming, binary data structures, network protocols (TCP/UDP/ICMP)
- **Note:** Requires administrator/root privileges

#### 12. TCP Client
**File:** `network/tcp_client.py`
- **Purpose:** Client-side socket programming with message transmission
- **Techniques:** TCP socket communication, hash verification
- **Use Case:** Network protocol understanding, client-server architecture
- **Skills:** Socket programming, network protocols

#### 13. TCP Server
**File:** `network/tcp_server.py`
- **Purpose:** Server-side socket programming with MD5 response
- **Techniques:** TCP socket listening, hash-based confirmation
- **Use Case:** Server architecture, message integrity verification
- **Skills:** Server programming, hash authentication concepts

---

### Text Analysis

#### 14. NLTK Corpus Analyzer
**File:** `text-analysis/nltk_corpus_analyzer.py`
- **Purpose:** Natural language processing for text corpus analysis
- **Techniques:** NLTK, word frequency, concordance, vocabulary analysis
- **Use Case:** Document analysis, keyword extraction, communication patterns
- **Skills:** NLP, text mining, statistical analysis

---

### Web Security

#### 15. Web Scraper & Reconnaissance Tool
**File:** `web-security/web_scraper.py`
- **Purpose:** Extract links and images from websites for security assessment
- **Techniques:** BeautifulSoup parsing, HTTP requests, web crawling
- **Use Case:** Reconnaissance, OSINT, web application analysis
- **Skills:** Web scraping, HTTP protocols, HTML parsing

---

### Cryptography

#### 16. Rainbow Table Generator
**File:** `cryptography/rainbow_table_generator.py`
- **Purpose:** Educational demonstration of password cracking via precomputed hashes
- **Techniques:** MD5 hashing, combinatorics, data serialization
- **Use Case:** Password security education, understanding hash attacks
- **Skills:** Cryptographic concepts, algorithm optimization, offensive security principles

---

### Steganography

#### 17. Image Steganography Tool
**File:** `steganography/image_steganography.py`
- **Purpose:** Embed covert messages in images using LSB steganography
- **Techniques:** Least Significant Bit manipulation, binary encoding, pixel modification
- **Use Case:** Covert communications, data hiding, digital watermarking
- **Skills:** Bit manipulation, image processing, offensive security concepts

---

### Malware Analysis

#### 18. VirusTotal Scanner
**File:** `malware-analysis/virustotal_scanner.py`
- **Purpose:** Automated malware scanning using VirusTotal API
- **Techniques:** Hash-based file identification, API integration, threat intelligence
- **Use Case:** Malware detection, file reputation checking, incident response
- **Skills:** API usage, hash algorithms, threat intelligence gathering


---


## 🔧 Technologies & Libraries Used

- **Python 3.x**
- **Standard Libraries:** os, socket, struct, re, hashlib, pickle, time, platform, uuid, logging
- **Third-Party:**
  - PrettyTable (data presentation)
  - Pillow/PIL (image processing)
  - BeautifulSoup (web parsing)
  - Requests (HTTP)
  - psutil (system information)
  - NLTK (natural language processing)
  - virustotal-api (malware scanning)

## 📚 Security Concepts Demonstrated

- Digital forensics methodology
- Memory analysis techniques
- File integrity verification
- Network packet analysis
- Socket programming (client-server architecture)
- Cryptographic hash functions
- Regular expression pattern matching
- Object-oriented security tool design
- Web reconnaissance techniques
- Chain of custody procedures
- Natural language processing for security
- Steganography and covert communications
- Malware analysis and threat intelligence
- API integration for security tools

## 🎓 Education

**Bachelor of Applied Science - Cyber Operations Engineering**  
University of Arizona (3.89 GPA)  
Graduation: December 2025

**Relevant Coursework:**
- Digital Forensics
- Security Programming
- Network Security
- Penetration Testing
- Incident Response
- Malware Analysis

## 🏆 Certifications

- ARRT - Radiologic Technology (R)
- ARRT - Computed Tomography (CT)


## 💼 Professional Experience

**Medical Device Security Analyst (Mitigation Specialist)** - HonorHealth (December 2025-Present)
- Medical device vulnerability management using ORDR platform
- ServiceNow security workflow automation
- Healthcare compliance and risk assessment
- Coordination with clinical teams for security patch deployment

**CT Technologist** - HonorHealth (July 2022-December 2025)
- HIPAA-compliant medical systems management
- RIS/PACS security and access control
- Healthcare IT infrastructure operations
- User access management and security coordination

## 🔗 Additional Projects

- Web Application Security Assessment (OWASP ZAP) - Penetration testing project

## ⚠️ Legal Disclaimer

These scripts are for educational and authorized security testing purposes only. Always obtain proper authorization before using security tools on systems you do not own or have explicit permission to test.

## 📧 Contact

- LinkedIn: https://www.linkedin.com/in/connor-stackhouse-91570986/
- Email: con.stackhouse@gmail.com
- GitHub: https://github.com/con-stackhouse

---

*Building secure systems through education and hands-on experience.*
```





