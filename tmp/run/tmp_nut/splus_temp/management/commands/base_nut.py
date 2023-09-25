def main ( ):
    from nuts.core import nut
    from .base_pool import pool
    from nuts.bots import bot
    from nuts.engines.contrib.splus import splus_engine

    bot = bot(
    splus_engine,
    "EgdmXGjEbuW4Uy6WFoxnvY_VuD4PfEYtxi2cC63wuSsKImBU1ygnaGv2Obid3fvaOOsNAub0ao83_oM47G7DF-wrSjRlwHgd3U0vCt0C0eKj4uLyZ6MpeAT4QvnaQPMkP-awI13pJPets_he"
    )

    my_nut = nut.base_nut(bot,pool) #type: ignore

    my_nut.run()
if __name__ =='__main__':
    main()