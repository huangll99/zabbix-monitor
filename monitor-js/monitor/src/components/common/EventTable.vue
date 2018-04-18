<template>
    <div id="eventTable">
        <el-table :data="events" stripe style="width: 100%">
            <el-table-column prop="time" label="时间" width="180"></el-table-column>
            <el-table-column prop="desc" label="事件" width="535"></el-table-column>
            <el-table-column label="严重等级" width="200">
                <template slot-scope="scope">
                    <Rate :value="scope.row.priority"></Rate>
                </template>
            </el-table-column>
        </el-table>
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
            self.refreshEvent();
            setInterval(function () {
                self.refreshEvent();
            }, 10000)
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
            },
            refreshEvent() {
                let self = this;
                self.$http.get('/api/event/').then((res) => {
                    self.events = res.data.map(function (event) {

                        if (event.trigger) {
                            return {
                                color: self.priorityColor(event.trigger.priority),
                                time: self.timeFormat(event.clock),
                                desc: self.trans(event.trigger.description, event.hosts),
                                acknowledged: event.acknowledged,
                                hosts: event.hosts,
                                priority: parseInt(event.trigger.priority)
                            }
                        } else {
                            return {
                                color: null
                            }
                        }

                    }).filter(function (event) {
                        return event.desc !=null;
                    }).splice(0, 10)
                })
            }
        }
    }
</script>
