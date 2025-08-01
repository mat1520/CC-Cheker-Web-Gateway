# Documentation - Demo Version
"""
DEMO FILE - API Documentation

Full version documentation includes:

API DOCUMENTATION:
- Complete endpoint reference
- Request/response examples
- Error code documentation
- Rate limiting details
- Authentication guide
- SDK documentation
- Integration examples
- Best practices guide

GATEWAY DOCUMENTATION:
- Setup instructions for each gateway
- Configuration examples
- Troubleshooting guides
- Performance optimization
- Security considerations

USER DOCUMENTATION:
- Getting started guide
- Feature overview
- Tutorial videos
- FAQ section
- Support resources

DEVELOPER DOCUMENTATION:
- Architecture overview
- Database schema
- Deployment guide
- Monitoring setup
- Backup procedures

Contact @mat1520 for complete documentation package.
"""

class APIDocs:
    """API Documentation - Demo version"""
    
    def __init__(self):
        self.demo_endpoints = {
            "POST /api/check": {
                "description": "Single card verification",
                "demo_note": "Full version processes real cards"
            },
            "POST /api/bulk": {
                "description": "Mass card processing",
                "demo_note": "Full version handles large file uploads"
            },
            "GET /api/bin/{bin}": {
                "description": "BIN lookup service",
                "demo_note": "Full version has real BIN database"
            }
        }
    
    def get_demo_docs(self):
        return {
            "api_version": "demo_v1",
            "endpoints": self.demo_endpoints,
            "demo_note": "Full version has comprehensive API documentation"
        }
