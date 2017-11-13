<template>
    <div id="events">

        <Timeline pending>
            <template v-for="event in events">
                <TimelineItem :color="event.color" v-if="event.color!=null">
                    <div class="time">{{event.time}}</div>
                    <div class="contents"></div>
                    <Alert type="warning" showIcon style="position: relative;">

                        <router-link :to="{path:'hostDetail',query:{hostid:event.hosts[0].hostid}}">{{event.desc}}</router-link>
                        <i-switch size="large" v-model="event.acknowledged!=0" style="position: absolute;right:10px;">
                            <span slot="close">确认</span>
                            <span slot="open">完成</span>
                        </i-switch>
                    </Alert>
                </TimelineItem>
            </template>
        </Timeline>
    </div>
</template>

<script>
    import moment from 'moment'

    export default {
        data() {
            return {
                events: [],
                msg: '确认',
                switch1: true
            }
        },
        created() {
            let self = this;
            self.$http.get('/api/event/').then((res) => {
                self.events = res.data.map(function (event) {

                    if(event.trigger){
                        return {
                            color: self.priorityColor(event.trigger.priority),
                            time: self.timeFormat(event.clock),
                            desc: self.trans(event.trigger.description, event.hosts),
                            acknowledged: event.acknowledged,
                            hosts:event.hosts
                        }
                    }else {
                        return {
                            color:null
                        }
                    }

                })
            })
        },
        methods: {
            priorityColor(priority) {
                switch (priority) {
                    case '1':
                        return 'green';
                    case '2':
                        return 'red';
                    case '3':
                        return 'yellow';
                    case '4':
                        return 'purple';
                    case '5':
                        return 'blue';
                }
            },
            timeFormat(time) {
                time = parseInt(time);
                return moment(time * 1000).format('YYYY/MM/DD') + ' ' + moment(time * 1000).format('HH:mm:ss')
            },
            trans(description, hosts) {

                let s = hosts.map(function (host) {
                    return host.host + ' ( ' + host.name + ' ) '
                }).join(',');
                return description.replace(/{HOST.NAME}/, s);
            }
        }
    }
</script>
<style scoped>
    .time {
        font-size: 14px;
        font-weight: bold;
    }

    .contents {
        padding-left: 5px;
    }


</style>
