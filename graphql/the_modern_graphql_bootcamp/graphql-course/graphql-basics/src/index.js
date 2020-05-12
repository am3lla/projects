import {GraphQLServer} from 'graphql-yoga'

//type definitions - schemas
const typeDefs =`
type Query {
    hello: String!
    name: String!
    location: String!
    bio: String!
}
`
//resolvers - functions
const resolvers = {
    Query: {
        hello: () =>  'This is my first query',
        name: () => 'Andreas',
        location: () => 'CDMX',
        bio: () => 'almost 40!'
    }
}

const server = new GraphQLServer(
    {
        typeDefs,
        resolvers
    }
)

server.start(()=> console.log('Server is running on localhost:4000'))