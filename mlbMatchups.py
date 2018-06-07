import requests
url = 'http://lookup-service-prod.mlb.com/json/named.stats_batter_vs_pitcher_composed.bam'

def matchupData(batter,pitcher,stat):
	params = {"sport_code":"'mlb'","game_type":"'R'","player_id":str(batter),"pitcher_id":str(pitcher)}
	return((requests.get(url, params = params).json())['stats_batter_vs_pitcher_composed']['stats_batter_vs_pitcher_total']['queryResults']['row'][stat])
