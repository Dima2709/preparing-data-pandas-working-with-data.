import pandas as pd

class data:

    def __init__(self,df):

        self.df = df

        self.df = pd.read_csv(self.df)

        self.df['profit'] = self.df['revenue']-self.df['budget']

        for i in range(len(self.df['release_year'])):
            mass = [j for j in self.df['release_year'][i] if j.isdigit()]
            self.df['release_year'][i] = int(''.join(mass))

#     # 1. У какого фильма из списка самый большой бюджет?
#     # 2. Какой из фильмов самый длительный (в минутах)?
#     # 6. Какой самый прибыльный фильм?

    def max(self, arg):

        return self.df.sort_values(by=arg).tail(1)

#     # 7. Какой фильм самый убыточный?
#     # 3. Какой из фильмов самый короткий(в минутах)?

    def min(self,arg):

        return self.df.sort_values(by=arg).head(1)

#     # 4. Какова средняя длительность фильмов?

    def avg(self,arg):

        print('В колонке -', arg,',', 'среднее значение = ', self.df[arg].mean())
        return self.df[arg].mean()

#     # 5. Каково медианное значение длительности фильмов?

    def med(self,arg):

        return self.df[arg].median()

#     #8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

    def count_dif(self):

        return self.df.query('revenue > budget').count()[0]

#     #9. Какой фильм оказался самым кассовым в 2008 году?

    def max_profit_years(self,arg):

        print(self.df.query(f'release_year == {arg}').sort_values(by='profit').tail(1))

#     #10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?

    def low_profit_years(self,arg,arg1):

        print(self.df.query(f'release_year >= {arg} & release_year <= {arg1}').sort_values(by='profit').head(1))

#     #11. Какого жанра фильмов больше всего?

    def genre_max(self):

        print((self.df[['genres']].apply(lambda x: x.str.split('|').explode())).value_counts().head(1))

#     #12. Фильмы какого жанра чаще всего становятся прибыльными?

    def genre_profit(self):

        print((self.df.query('profit>0')[['genres']].apply(lambda x: x.str.split('|').explode())).value_counts().head(1))

#     #13. У какого режиссера самые большие суммарные кассовые сбооры?

    def dir_win(self):

        print(self.df[['director', 'profit']].groupby(['director']).sum().sort_values(by='profit').tail(1))

#     #14. Какой режисер снял больше всего фильмов в стиле Action?

    def dir_genre(self,arg):

        df1 = pd.concat([self.df.director, self.df[['genres']].apply(lambda x: x.str.split('|').explode())], axis=1)
        df1[(df1.genres == 'Action')].groupby('director').count().sort_values(by='genres').idxmax()

#     #15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?

    def cast_profit(self,arg):

        print(pd.concat([self.df[(self.df.release_year == arg)][['cast']].apply(lambda x: x.str.split('|').explode()),
                   self.df[(self.df.release_year == arg)].profit], axis=1).groupby('cast').sum().sort_values(by='profit').tail(1))

#     #16. Какой актер снялся в большем количестве высокобюджетных фильмов?

    def cast_bud(self):

        print(self.df[(self.df['budget'] > self.df['budget'].sum() / self.df['budget'].count())][['cast']].apply(
            lambda x: x.str.split('|').explode()).value_counts().head(1))

#     #17. В фильмах какого жанра больше всего снимался Nicolas Cage?

    def gen_cast(self,arg):

        df1 = self.df[['cast']].apply(lambda x: x.str.split('|').explode())
        df2 = self.df[['genres']].apply(lambda x: x.str.split('|').explode())
        print(df1.cast[(df1.cast == arg)].to_frame().join(df2.genres).value_counts().head(1))

#     #18. Самый убыточный фильм от Paramount Pictures

    def low_profit_com(self,arg):

        df1 = pd.concat([self.df[['production_companies']].apply(lambda x: x.str.split('|').explode()), self.df.profit], axis=1)
        print(self.df.iloc[df1[(df1.production_companies == 'Paramount Pictures')].sort_values(by='profit').head(1).index[0]])

#     #19. Какой год стал самым успешным по суммарным кассовым сборам?

    def years_prof(self):

        print(pd.concat([self.df.release_year, self.df.profit],axis=1).groupby('release_year').sum().sort_values(by='profit').tail(1))

#     #20. Какой самый прибыльный год для студии Warner Bros?

    def comp_max_year(self,arg):

        df1 = self.df[['production_companies']].apply(lambda x: x.str.split('|').explode())
        print(df1[(df1.production_companies == arg)].production_companies.to_frame().join(self.df['release_year']).join(
            self.df['profit']).groupby('release_year').sum().sort_values(by='profit').tail(1))

#     #21. В каком месяце за все годы суммарно вышло больше всего фильмов?

    def moun_count_film(self):

        print(pd.DatetimeIndex(self.df['release_date']).month.value_counts().sort_values().tail(1))

#     #22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

    def count_film_moun(self):

        print(pd.DatetimeIndex(self.df['release_date']).month.value_counts().loc[[6,7,8]].sum())

#     #23. Для какого режиссера зима – самое продуктивное время года?

    def dir_winter(self):

        print(self.df.director.to_frame().join(pd.Series(pd.DatetimeIndex(self.df['release_date']).month))
              .query('release_date == 12 | release_date == 1 | release_date == 2')
              .groupby('director').count().sort_values(by='release_date').tail(1))

#     #24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

    def comp_len_title(self):

        print(self.df[['production_companies']].apply(lambda x: x.str.split('|').explode()).production_companies.to_frame()
              .join(self.df['original_title'].apply(lambda x: len(x))).groupby('production_companies').sum().sort_values(by='original_title').tail(1))

#     #25. названия фильмов какой студии в среднем самые длинные по количеству слов?

    def word_metr(self,arg):

        print(self.df[['production_companies']].apply(lambda x: x.str.split('|').explode()).production_companies.to_frame().join(
            self.df['original_title'].apply(lambda x: len(x.split(' ')))).groupby('production_companies').mean().sort_values(
            by='original_title').tail(1))

#     #26. Какие фильмы входят в 1 процент лучших по рейтингу?

    def prec_rait(self,arg):

        print(self.df.sort_values(by = 'vote_average').tail(int(len(self.df)*arg/100)))

#     #27. Какие актеры чаще всего снимаются в одном фильме вместе?

    def cast_tog(self):

        print(self.df['cast'].value_counts().index[0], ' - ', self.df['cast'].value_counts().max())

        mass = []
        mass2 = []
        for i in self.df['cast']:
            mass.append(i.split('|'))

        for i in range(len(mass)):

            if len(mass[i]) == 3:
                mass2.append(mass[i])
                count = 0
                for l in range(3):
                    for j in range(1, 3):
                        if count == 0:
                            mass2.append([mass[i][l], mass[i][j]])
                            count += 1
                        elif count == 1:
                            mass2.append([mass[i][l], mass[i][j]])
                            mass2.append([mass[i][1], mass[i][2]])
                            count += 1

            elif len(mass[i]) == 4:
                mass2.append(mass[i])
                count = 0
                for o in range(4):
                    for j in range(1, 4):
                        for k in range(2, 4):
                            if o == 0:
                                if count == 0:
                                    mass2.append([mass[i][o], mass[i][j], mass[i][k]])
                                    mass2.append([mass[i][o], mass[i][j]])
                                    count += 1
                                elif count == 1:
                                    mass2.append([mass[i][o], mass[i][j], mass[i][k]])
                                    count += 1
                                elif count == 3:
                                    mass2.append([mass[i][o], mass[i][j], mass[i][k]])
                                    mass2.append([mass[i][o], mass[i][k]])
                                    count += 1
                                elif count == 2:
                                    mass2.append([mass[i][o], mass[i][j]])
                                    count += 1
                            elif o == 1:
                                if count == 4:
                                    mass2.append([mass[i][o], mass[i][k]])
                                    count += 1
                                elif count == 5:
                                    mass2.append([mass[i][o], mass[i][k]])
                                    count += 1
                                elif count == 6:
                                    count += 1
                                elif count == 7:
                                    mass2.append([mass[i][o], mass[i][j], mass[i][k]])
                                    mass2.append([mass[i][j], mass[i][k]])
                                    count += 1
                                elif count == 8:
                                    break
            elif len(mass[i]) == 5:
                count = 0
                mass2.append(mass[i])
                for p in range(5):
                    for j in range(1, 5):
                        for k in range(2, 5):
                            for l in range(3, 5):
                                if p == 0:
                                    if count == 0:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k]])
                                        mass2.append([mass[i][p], mass[i][j], mass[i][l]])
                                        mass2.append([mass[i][p], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][p], mass[i][j]])
                                        mass2.append([mass[i][p], mass[i][k]])
                                        mass2.append([mass[i][p], mass[i][l]])
                                        mass2.append([mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][j], mass[i][k]])
                                        mass2.append([mass[i][j], mass[i][l]])
                                        mass2.append([mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 1:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][p], mass[i][l]])
                                        mass2.append([mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][j], mass[i][l]])
                                        mass2.append([mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 2:
                                        count += 1
                                    elif count == 3:
                                        mass2.append([mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 4:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k]])
                                        mass2.append([mass[i][p], mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 5:
                                        count += 1
                                    elif count == 6:
                                        count += 1
                                    elif count == 7:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][l]])
                                        count += 1
                                    elif count == 8:
                                        count += 1
                                    elif count == 9:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        mass2.append([mass[i][j], mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 10:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        count += 1

                                elif p == 1 and j == 2 and k == 3 and l == 4:
                                    if count == 11:
                                        mass2.append([mass[i][p], mass[i][j], mass[i][k], mass[i][l]])
                                        count += 1
                                    elif count == 12:
                                        break
        for i in mass2:
            i = i.sort()
        a = {}
        for i in range(len(mass2)):
            a[','.join(mass2[i])] = 0
        for i in mass2:
            if ','.join(i) in a.keys():
                a[','.join(i)] +=1
        for i in list(a.keys()):
            if a[i] == max(a.values()):
                print(i, ' - ', a[i])



the = data('data1.csv')
#the.max('budget')
#the.min('runtime')
#the.avg('runtime')
#the.med('runtime')
#the.count_dif()
#the.max_profit_years(2008)
#the.low_profit_years(2012, 2014)
#the.genre_max()
#the.genre_profit()
#the.dir_win()
#the.dir_genre('Action')
#the.cast_profit(2012)
#the.cast_bud()
#the.gen_cast('Nicolas Cage')
#the.low_profit_com('Paramount Pictures')
#the.years_prof()
#the.comp_max_year('Warner Bros.')
#the.moun_count_film()
#the.count_film_moun()
#the.dir_winter()
#the.comp_len_title()
#the.prec_rait(1)
#the.word_metr('original_title')
#the.cast_tog()
