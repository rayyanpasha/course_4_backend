// const { ApolloServer } = require('apollo-server');
// const typeDefs = require('./schema2');
// const resolvers = require('./resolver2');

// const server = new ApolloServer({typeDefs, resolvers});


// server.listen().then(({ url }) => {
//     console.log(` Server ready at ${url}`);
// });
const { ApolloServer } = require('apollo-server');

const typeDefs = require('./schema2');

const resolvers = require('./resolver2');

const server = new ApolloServer({

  typeDefs,

  resolvers,

  context: ({ req }) => {

    const authHeader = req.headers.authorization || "";

    const token = authHeader.replace("Bearer ", "").trim();

    return { token };

  }

});

server.listen().then(({ url }) => {

  console.log(`🚀 Server ready at ${url}`);

});