from django.mainsite.patient_service import env


class DBRouter:

    def db_for_read(self, model, **hints):
        return self.select_db()

    def db_for_write(self, model, **hints):
        return self.select_db()

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'test' or obj2._meta.app_label == 'test':
            return None
        return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if env.env_list.get('ENV') == 'dockerized':
    #         return db == 'dockerized'
    #     return db == 'local'

    def select_db(self):
        if env.env_list.get('ENV') is not None:
            return env.env_list.get('ENV')
        return 'local'
