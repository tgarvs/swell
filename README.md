Trying to make a normal webdev project lol

Having Claude help me understand the concepts...I do the coding



Week 1 — FastAPI + Swell API Integration
Goal: A working backend that fetches, processes, and serves forecast data.
Subproblems:

Pick your forecast API (Stormglass is the best free option — gives swell height, period, direction, wind, tide in one call)
Set up FastAPI project structure — routers, schemas, basic /health endpoint so you understand the pattern
Model your data with Pydantic — define what a ForecastPoint, SpotConditions, SwellComponent looks like as a typed schema
Write the Stormglass fetch layer — handle auth, rate limits, error responses
Process raw hourly data into something useful — aggregate to sessions (dawn, morning, afternoon), pull out the relevant parameters
Store a static list of Irish spots as JSON (name, lat/lng, characteristics) — Lahinch, Bundoran, Mullaghmore, Rossnowlagh etc.
Expose a GET /forecast/{spot_id} endpoint that returns clean processed data
Write a few basic pytest tests for your data processing logic — you'll need these for CI later


Week 2 — React Frontend
Goal: A usable UI that displays forecast data clearly.
Subproblems:

Bootstrap a React app with Vite (not Create React App — Vite is current)
Set up Tailwind
Build a spot selector component — dropdown or card grid of Irish spots
Fetch from your FastAPI backend — learn useEffect, fetch/axios, loading states, error handling
Swell height chart over 48hrs — Recharts AreaChart, get comfortable with data transformation for charting
Wind component — direction + speed, probably a simple table or icon-based display
Tide timeline — this is a bit fiddly, a simple line chart works fine
"Session window" cards — morning/afternoon blocks with a quick summary of the key numbers
Basic responsive layout so it works on mobile (you'll check it on the beach)


Week 3 — LangChain RAG Chain
Goal: AI-generated plain-English session recommendation per spot.
Subproblems:

Set up LangChain + OpenAI in your FastAPI backend
Build your spot knowledge base — write a paragraph per spot describing it (works best on X tide, needs N swell direction, sheltered from SW wind, etc.) — this is your RAG "documents"
Embed and index spot documents — FAISS locally is fine, no need for a vector DB yet
Design your prompt chain — retrieve relevant spot doc, inject current forecast data, prompt for a recommendation in a specific format
Handle the output structure — you want something like {overall_rating, best_window, reasoning, warnings} so the frontend can display it nicely
Add a GET /recommendation/{spot_id} endpoint that runs the chain
Wire it into the frontend — a recommendation card that loads async after the forecast data


Week 4 — CI/CD, Deployment, Polish
Goal: Shipped, shareable, on your resume.
Subproblems:

Write a Dockerfile for the FastAPI backend
GitHub Actions workflow — on push to main: run pytest, lint with ruff, build Docker image
Deploy backend to Render (free tier, connects directly to your GitHub repo)
Deploy frontend to Vercel (even simpler — just connects to repo)
Environment variable management — API keys in GitHub Secrets, not in code
CORS configuration between your deployed frontend and backend
Write a proper README — architecture diagram, setup instructions, live demo link
Draft your resume bullet points while it's fresh