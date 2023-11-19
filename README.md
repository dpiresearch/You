# You.com api

Experimenting with the you.com api.  The query hardcoded here asks for Amazon links to computer monitor recommendations.  We want to see if we get actual shopping links.

## Overview

Execution:
% python first.py

This will hit the 'search' and 'rag' endpoints of you.com

The 'rag' endpoint is closer to what the frontend you.com results produce.  The snippets coming back are the chunks that the you.com
backend has already done for their own RAG infrastructure.

The 'search' endpoint is more pure search ( external LLM? )

## Output

The way it's configured now, the output will show the url associated with the answer.  For search endpoint, the Amazon links are usually hallucinations and will lead to "Page Not Found" or a non product detail link.  For the rag endpoint, the urls will lead to real pages, but not to actual Amazon product pages.


