import argparse
import os
import json
import pandas as pd
import requests
import time
from src.serper_wrapper import SerperClient

# Placeholder for Crawl4AI until installed/verified
# from crawl4ai import AsyncWebCrawler

def setup_args():
    parser = argparse.ArgumentParser(description="Lead Generation Pipeline")
    parser.add_argument('--strategy', choices=['LOCAL', 'B2B'], required=True)
    parser.add_argument('--niche', required=True, help="e.g. 'Coffee Shop' or 'SaaS'")
    parser.add_argument('--location', required=True, help="e.g. 'Austin, TX'")
    parser.add_argument('--role', help="Required for B2B, e.g. 'CTO'")
    return parser.parse_args()

def run_local_strategy(niche, location, serper_client):
    print(f"[*] Running LOCAL strategy for '{niche}' in '{location}'...")
    
    # 1. Discovery (Serper Maps)
    query = f"{niche} in {location}"
    print(f"    -> Searching Google Maps for: {query}")
    results = serper_client.places_search(query)
    
    places = results.get("places", [])
    print(f"    -> Found {len(places)} places.")
    
    enriched_leads = []
    
    for place in places[:5]: # Limit for testing
        lead = {
            "name": place.get("title"),
            "address": place.get("address"),
            "website": place.get("website"),
            "phone": place.get("phoneNumber"),
            "rating": place.get("rating")
        }
        
        if not lead['website']:
            continue
            
        print(f"    -> Processing {lead['name']} ({lead['website']})...")
        
        # 2. Qualification (Mock / Crawl4AI)
        # In real impl, use Crawl4AI to find IG link
        # ig_link = crawl4ai.find_social_url(lead['website'], 'instagram')
        ig_link = None # Placeholder
        
        # Fallback Check
        if not ig_link:
             # Basic heuristic or fallback search could go here
             pass

        if ig_link:
            # 3. Enrichment (Olostep)
            print(f"       -> Scraping Instagram: {ig_link}")
            api_key = os.getenv('OLOSTEP_API_KEY')
            if api_key:
                try:
                    # Quick inline Olostep call (or could import from skill if valid python module, but script is standalone)
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    resp = requests.post("https://api.olostep.com/v1/scrapes", json={"url": ig_link}, headers=headers)
                    resp.raise_for_status()
                    data = resp.json()
                    # print(f"       -> Olostep Data: {str(data)[:100]}...") # Debug
                    # basic parsing example - depends on olostep structure
                    lead['olostep_data'] = data
                except Exception as e:
                    print(f"       -> Olostep Error: {e}")
            else:
                print("       -> OLOSTEP_API_KEY not set, skipping enrichment.")
            
        lead['type'] = 'LOCAL'
        enriched_leads.append(lead)
            
    return enriched_leads

def run_b2b_strategy(niche, location, role, serper_client):
    if not role:
        raise ValueError("Role is required for B2B strategy")
        
    print(f"[*] Running B2B strategy for '{role}' in '{niche}' ({location})...")
    
    # 1. Discovery (Serper X-Ray)
    results = serper_client.xray_search(role, niche, location)
    organic = results.get("organic", [])
    print(f"    -> Found {len(organic)} profiles.")
    
    enriched_leads = []
    
    for item in organic[:5]:
        lead = {
            "name": item.get("title"), # Often contains Name - Role - Company
            "link": item.get("link"),
            "snippet": item.get("snippet")
        }
        
        # 2. Enrichment (Olostep LinkedIn)
        # Warning: LinkedIn is tough. Olostep might help if profile is public.
        # print(f"    -> Enriching Profile: {lead['link']}")
        # if os.getenv('OLOSTEP_API_KEY'):
             # Similar Olostep call...
        #    pass
        
        lead['type'] = 'B2B'
        enriched_leads.append(lead)
        
    return enriched_leads

def main():
    args = setup_args()
    
    # Check Env
    if not os.getenv("OLOSTEP_API_KEY"):
        print("Warning: OLOSTEP_API_KEY not set. Enrichment will be skipped.")
    
    if not os.getenv("SERPER_API_KEY"):
        print("Error: SERPER_API_KEY not set.")
        return


    serper_client = SerperClient()
    
    if args.strategy == 'LOCAL':
        results = run_local_strategy(args.niche, args.location, serper_client)
    else:
        results = run_b2b_strategy(args.niche, args.location, args.role, serper_client)
        
    # Save
    if results:
        df = pd.DataFrame(results)
        print("\n[*] Results:")
        print(df)
        df.to_csv("leads_output.csv", index=False)
        print(f"[*] Saved {len(df)} leads to leads_output.csv")
    else:
        print("[*] No leads found.")

if __name__ == "__main__":
    main()
