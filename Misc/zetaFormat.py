import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")


garbage =\
"1230	maimai	
VIIIbit Explorer 	DX	
BASIC
	
6
		225	88.23%	8	3.13%	4	1.56%	9	3.52%	9	3.52%	255 	188	-	Splash+ (煌)",
1230	maimai	
VIIIbit Explorer 	DX	
ADVANCED
	
8
		351	82.78%	20	4.71%	14	3.3%	29	6.83%	10	2.35%	424 	188	-	Splash+ (煌)
1230	maimai	
VIIIbit Explorer 	DX	
EXPERT
	
13
	13	606	73.45%	75	9.09%	72	8.72%	46	5.57%	26	3.15%	825 	188	Jack	Splash+ (煌)
1230	maimai	
VIIIbit Explorer 	DX	
MASTER
	
14+
	14.7	738	73.87%	28	2.8%	75	7.5%	70	7%	88	8.8%	999 	188	-ZONE- SaFaRi	Splash+ (煌)
1212	ゲーム＆バラエティ	
Luminaria 	DX	
BASIC
	
5
		143	69.41%	6	2.91%	8	3.88%	42	20.38%	7	3.39%	206 	227	-	FESTiVAL
1212	ゲーム＆バラエティ	
Luminaria 	DX	
ADVANCED
	
7+
		282	79.88%	18	5.09%	4	1.13%	42	11.89%	7	1.98%	353 	227	-	FESTiVAL
1212	ゲーム＆バラエティ	
Luminaria 	DX	
EXPERT
	
12
	12.2	481	69.6%	55	7.95%	17	2.46%	63	9.11%	75	10.85%	691 	227	翠楼屋	FESTiVAL
1212	ゲーム＆バラエティ	
Luminaria 	DX	
MASTER
	
13+
	13.9	640	76.92%	46	5.52%	83	9.97%	18	2.16%	45	5.4%	832 	227	小鳥遊さん	FESTiVAL
1211	ゲーム＆バラエティ	
Random 	DX	
BASIC
	
3
		131	77.05%	17	10%	12	7.05%	5	2.94%	5	2.94%	170 	132	-	FESTiVAL
1211	ゲーム＆バラエティ	
Random 	DX	
ADVANCED
	
7
		218	83.2%	13	4.96%	7	2.67%	16	6.1%	8	3.05%	262 	132	-	FESTiVAL
1211	ゲーム＆バラエティ	
Random 	DX	
EXPERT
	
11
		302	63.17%	98	20.5%	29	6.06%	30	6.27%	19	3.97%	478 	132	ロシェ＠ペンギン	FESTiVAL
1211	ゲーム＆バラエティ	
Random 	DX	
MASTER
	
13
	13.5	417	53.05%	119	15.13%	57	7.25%	147	18.7%	46	5.85%	786 	132	ぴちネコ	FESTiVAL
1210	maimai	
mystique as iris
	DX	
BASIC
	
5
													172	-	FESTiVAL
1210	maimai	
mystique as iris
	DX	
ADVANCED
	
9+
													172	-	FESTiVAL
1210	maimai	
mystique as iris
	DX	
EXPERT
	
12+
	12.8	441	59.43%	118	15.9%	58	7.81%	54	7.27%	71	9.56%	742 	172	翠楼屋	FESTiVAL
1210	maimai	
mystique as iris
	DX	
MASTER
	
14+
	14.7	829	71.03%	88	7.54%	75	6.42%	113	9.68%	62	5.31%	1167 	172	red phoenix	FESTiVAL
1209	ゲーム＆バラエティ	
田中 	DX	
BASIC
	
5
		139	74.73%	29	15.59%	6	3.22%	7	3.76%	5	2.68%	186 	186	-	FESTiVAL
1209	ゲーム＆バラエティ	
田中 	DX	
ADVANCED
	
8
		284	79.1%	24	6.68%	7	1.94%	34	9.47%	10	2.78%	359 	186	-	FESTiVAL
1209	ゲーム＆バラエティ	
田中 	DX	
EXPERT
	
12
	12	464	70.19%	74	11.19%	28	4.23%	81	12.25%	14	2.11%	661 	186	翠楼屋	FESTiVAL
1209	ゲーム＆バラエティ	
田中 	DX	
MASTER
	
14
	14.3	571	64.01%	85	9.52%	80	8.96%	110	12.33%	46	5.15%	892 	186	ぴちネコ	FESTiVAL
1208	東方Project	
スカーレット警察のゲットーパトロール24時 	DX	
BASIC
	
3
		88	75.21%	9	7.69%	8	6.83%	10	8.54%	2	1.7%	117 	160	-	FESTiVAL
1208	東方Project	
スカーレット警察のゲットーパトロール24時 	DX	
ADVANCED
	
7
		189	75%	17	6.74%	12	4.76%	18	7.14%	16	6.34%	252 	160	-	FESTiVAL
1208	東方Project	
スカーレット警察のゲットーパトロール24時 	DX	
EXPERT
	
9
		172	56.02%	51	16.61%	28	9.12%	18	5.86%	38	12.37%	307 	160	じゃこレモン	FESTiVAL
1208	東方Project	
スカーレット警察のゲットーパトロール24時 	DX	
MASTER
	
13
	13.5	519	72.99%	31	4.36%	77	10.82%	49	6.89%	35	4.92%	711 	160	はっぴー	FESTiVAL
1207	niconico＆ボーカロイド	
EYE 	DX	
BASIC
	
2
		71	65.13%	6	5.5%	4	3.66%	8	7.33%	20	18.34%	109 	137	-	FESTiVAL
1207	niconico＆ボーカロイド	
EYE 	DX	
ADVANCED
	
6
		267	79.7%	12	3.58%	22	6.56%	26	7.76%	8	2.38%	335 	137	-	FESTiVAL
1207	niconico＆ボーカロイド	
EYE 	DX	
EXPERT
	
9
	9	386	80.24%	57	11.85%	22	4.57%	3	0.62%	13	2.7%	481 	137	Jack	FESTiVAL
1207	niconico＆ボーカロイド	
EYE 	DX	
MASTER
	
12+
	12.9	448	56.35%	41	5.15%	69	8.67%	151	18.99%	86	10.81%	795 	137	サファ太 vs 翠楼屋	FESTiVAL
1206	niconico＆ボーカロイド	
ヴィラン 	DX	
BASIC
	
2
		71	78.88%	5	5.55%	4	4.44%	8	8.88%	2	2.22%	90 	102	-	FESTiVAL
1206	niconico＆ボーカロイド	
ヴィラン 	DX	
ADVANCED
	
6
		173	74.24%	24	10.3%	5	2.14%	24	10.3%	7	3%	233 	102	-	FESTiVAL
1206	niconico＆ボーカロイド	
ヴィラン 	DX	
EXPERT
	
9
	9.2	270	71.61%	63	16.71%	20	5.3%	17	4.5%	7	1.85%	377 	102	はっぴー	FESTiVAL
1206	niconico＆ボーカロイド	
ヴィラン 	DX	
MASTER
	
11+
	11.8	398	69.58%	44	7.69%	67	11.71%	48	8.39%	15	2.62%	572 	102	緑風 犬三郎	FESTiVAL
1206	niconico＆ボーカロイド	
ヴィラン 	DX	
Re:MASTER
	
13
	13	431	63.47%	33	4.86%	55	8.1%	111	16.34%	49	7.21%	679 	102	カマボコ君	FESTiVAL
1205	niconico＆ボーカロイド	
フォニイ 	DX	
BASIC
	
2
		78	64.46%	16	13.22%	6	4.95%	15	12.39%	6	4.95%	121 	170	-	FESTiVAL
1205	niconico＆ボーカロイド	
フォニイ 	DX	
ADVANCED
	
6
		242	79.86%	23	7.59%	11	3.63%	21	6.93%	6	1.98%	303 	170	-	FESTiVAL
1205	niconico＆ボーカロイド	
フォニイ 	DX	
EXPERT
	
9+
	9.8	370	71.15%	53	10.19%	9	1.73%	64	12.3%	24	4.61%	520 	170	畳返し	FESTiVAL
1205	niconico＆ボーカロイド	
フォニイ 	DX	
MASTER
	
11
	11.5	434	69.77%	43	6.91%	89	14.3%	30	4.82%	26	4.18%	622 	170	緑風 犬三郎	FESTiVAL
1205	niconico＆ボーカロイド	
フォニイ 	DX	
Re:MASTER
	
13
	13.3	501	66.53%	46	6.1%	119	15.8%	44	5.84%	43	5.71%	753 	170	はっぴー	FESTiVAL
1204	POPS＆アニメ	
残響散歌 	DX	
BASIC
	
3
		117	72.22%	12	7.4%	4	2.46%	22	13.58%	7	4.32%	162 	171	-	FESTiVAL
1204	POPS＆アニメ	
残響散歌 	DX	
ADVANCED
	
6
		295	79.08%	17	4.55%	7	1.87%	46	12.33%	8	2.14%	373 	171	-	FESTiVAL
1204	POPS＆アニメ	
残響散歌 	DX	
EXPERT
	
9+
	9.7	370	67.64%	57	10.42%	50	9.14%	32	5.85%	38	6.94%	547 	171	翠楼屋	FESTiVAL
1204	POPS＆アニメ	
残響散歌 	DX	
MASTER
	
13+
	13.7	657	69.96%	38	4.04%	199	21.19%	22	2.34%	23	2.44%	939 	171	Jack	FESTiVAL
1203	POPS＆アニメ	
踊 	DX	
BASIC
	
2
		91	66.42%	9	6.56%	4	2.91%	24	17.51%	9	6.56%	137 	128	-	FESTiVAL
1203	POPS＆アニメ	
踊 	DX	
ADVANCED
	
6
		239	75.87%	24	7.61%	12	3.8%	29	9.2%	11	3.49%	315 	128	-	FESTiVAL
1203	POPS＆アニメ	
踊 	DX	
EXPERT
	
8
	8.5	337	70.35%	34	7.09%	63	13.15%	27	5.63%	18	3.75%	479 	128	はっぴー	FESTiVAL
1203	POPS＆アニメ	
踊 	DX	
MASTER
	
11
	11.5	468	66.19%	58	8.2%	78	11.03%	70	9.9%	33	4.66%	707 	128	緑風 犬三郎	FESTiVAL
1203	POPS＆アニメ	
踊 	DX	
Re:MASTER
	
13
	13.2	536	63.58%	42	4.98%	71	8.42%	113	13.4%	81	9.6%	843 	128	あまくちジンジャー	FESTiVAL
1202	niconico＆ボーカロイド	
ジレンマ 	DX	
BASIC
	
3
		129	80.12%	12	7.45%	6	3.72%	11	6.83%	3	1.86%	161 	188	-	FESTiVAL

...


#print(garbage)
#garbageNew = ""
#garbageNew = garbageNew.join(garbage.split())
#print (garbageNew)




garbageNew = _RE_COMBINE_WHITESPACE.sub("   ", garbage).strip()
print(garbageNew)