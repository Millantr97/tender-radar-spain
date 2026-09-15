from pathlib import Path

p=Path(__file__).parents[1]/'.github/workflows/refresh-data.yml';s=p.read_text();s=s.replace("'17 */6 * * *'→ Runs at 17 minutes past the hour, every 6 hours","'17 */6 * * *'");p.write_text(s)
